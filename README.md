# QGIS

## Overview

**Industry**: Geospatial Information Systems

**Target Container OS**: Linux

**License**: Open Source

**Website**: https://qgis.org/en/site/

**Github**: https://github.com/qgis/QGIS

## Notes

This is a GUI application that requires a reverse proxy.

```
docker build -t qgis .
docker run --rm -d -p 8888:8888 qgis
```