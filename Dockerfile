# get the caddy executable
FROM caddy AS caddy-build

FROM connextproject/vector_router:0.2.5-beta.18 as router-layer

FROM connextproject/vector_node:0.2.5-beta.18 as ide-build

RUN apk update && \
    apk add git openssh bash python3 python3-dev py-pip make gcc g++ libx11-dev libxkbfile-dev supervisor && \
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && \
    apk add nodejs npm

# create a build directory for the IDE
RUN mkdir /theia
WORKDIR /theia

# build the IDE
COPY package.json .
COPY preload.html .
RUN yarn --pure-lockfile && \
    NODE_OPTIONS="--max_old_space_size=4096" yarn theia build && \
    yarn theia download:plugins && \
    yarn --production && \
    yarn autoclean --init && \
    echo *.ts >> .yarnclean && \
    echo *.ts.map >> .yarnclean && \
    echo *.spec.* >> .yarnclean && \
    yarn autoclean --force && \
    yarn cache clean
	
# Final build stage
# FROM connextproject/vector-node:0.2.5-beta.18 as final
FROM connextproject/vector_node:0.2.5-beta.18

RUN apk update && \
    apk add git zip unzip openssh bash python3 python3-dev py-pip make gcc g++ libx11-dev libxkbfile-dev supervisor && \
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && \
    apk add nodejs npm && \
	curl https://rclone.org/install.sh | bash 

# add galileo non-root user
RUN adduser -S galileo
COPY .theia /home/galileo/.theia
COPY .vscode /home/galileo/.vscode
RUN chmod a+rwx /home/galileo/.theia
RUN chmod a+rwx /app

# edit the node configuration file for operating as a relay node
RUN mkdir /theia
WORKDIR /theia

# switch to non-root user
#USER galileo
WORKDIR /theia

# get the IDE
COPY --from=ide-build /theia /theia
COPY --from=router-layer /app /router/app
	
# get superviserd
COPY supervisord.conf /etc/
# copy node.config
COPY node.config.json /app/config.json
# copy router.config
COPY router.config.json /router/app/config.json

# set environment variable to look for plugins in the correct directory
# set environment variable to look for plugins in the correct directory
ENV SHELL=/bin/bash \
    THEIA_DEFAULT_PLUGINS=local-dir:/theia/plugins
ENV USE_LOCAL_GIT true

# get the Caddy server executable
# copy the caddy server build into this container
COPY --from=caddy-build /usr/bin/caddy /usr/bin/caddy
COPY Caddyfile /etc/

# Vector environment variables
RUN mkdir /database
ENV VECTOR_PROD true
ENV VECTOR_SQLITE_FILE "/database/store.db"

# # set login credintials and write them to text file
ENV USERNAME "a"
ENV PASSWORD "a"
RUN echo "basicauth /* {" >> /tmp/hashpass.txt && \
    echo "    {env.USERNAME}" $(caddy hash-password -plaintext $(echo $PASSWORD)) >> /tmp/hashpass.txt && \
    echo "}" >> /tmp/hashpass.txt

ENTRYPOINT ["sh", "-c", "supervisord"]