vector-tile-base
================

This library encodes and decodes [Mapbox Vector Tiles](https://github.com/mapbox/vector-tile-spec). It is intended for use by developers with clear understanding of the Vector Tile format. The code is written as a pure python implementation with support of the google protobuf python format. 

## For compatibility with protobuf 4.21.1
Regenerate the protobuf files from the protobuf definitions.

Get the right version of protoc included in grpcio-tools

```bash
pip install grpcio-tools
```


```bash
python -m grpc_tools.protoc -I. --python_out=vector_tile_base vector_tile.proto
```


## Features

- ✅ **Python 3.11+ Support**: Fully compatible with modern Python versions
- ✅ **Vector Tile Version 2**: Standard vector tile encoding/decoding
- ✅ **Vector Tile Version 3**: Extended support for 3D geometry, splines, and inline values
- ✅ **Modern Build System**: Uses `pyproject.toml` for modern Python packaging
- ✅ **Enhanced Protobuf**: Updated protobuf definitions with new fields for version 3

## New in Version 3 Support

- **3D Geometry**: Support for elevation data in features
- **SPLINE Geometry**: Smooth curve geometry type
- **Inline Values**: Efficient encoding of complex data types
- **String Values**: Enhanced string attribute support
- **Geometric Attributes**: Attributes tied to geometry
- **Scaling**: Automatic data scaling for optimization
- **Tile Location**: Metadata about tile position (x, y, z)

## Depends

 - Google protobuf python bindings (>=3.20.0)

## Installation

### Modern Installation (Recommended)

```bash
pip install .
```

### Development Installation

```bash
pip install -e .
```

## Development

To run tests use [pytest](https://docs.pytest.org/en/latest/):

```bash
pytest
```

## Example

Some very simple code examples

### Encode

There is an example encoding provided in `examples` and can be used to encode a `.mvt` file.

```bash
python examples/encode.py my.mvt
```

```python
import vector_tile_base
import sys

vt = vector_tile_base.VectorTile()
layer = vt.add_layer('my_locations')
feature = layer.add_point_feature()
feature.add_points([[10,10],[20,20]])
feature.id = 1
feature.attributes = { 'type': 1, 'name': 'my_points' }

encoded_tile = vt.serialize()

f = open(sys.argv[1], "wb")
f.write(encoded_tile)
f.close()
```

### Decode

There is an example decoding provided in `examples` and can be used to decode a `.mvt` file.

```bash
python examples/decode.py my.mvt
```

```python
import vector_tile_base
import sys

f = open(sys.argv[1], "rb")
raw_tile = f.read()
f.close()

vt = vector_tile_base.VectorTile(raw_tile)
for l in vt.layers:
    print(l.name)
    for f in l.features:
        print(f.type)
        print(f.attributes)
        print(f.get_geometry())
```

### Version 3 Features Example

```python
import vector_tile_base

# Create a version 3 tile with 3D support
vt = vector_tile_base.VectorTile()
layer = vt.add_layer('my_3d_layer', version=3)

# Add 3D point feature
feature = layer.add_point_feature(has_elevation=True)
feature.add_points([[10, 20, 100]])  # x, y, z coordinates
feature.attributes = {'height': 100, 'name': 'mountain_peak'}

# Add spline feature
spline_feature = layer.add_spline_feature(degree=3)
control_points = [[0, 0], [10, 10], [20, 0]]
knots = [0, 0, 0, 1, 1, 1]
spline_feature.add_spline(control_points, knots)

encoded_tile = vt.serialize()
```

## Migration from Version 1.0.1

The main changes in this update:

1. **Modern Python Support**: Now requires Python 3.9+
2. **Updated Dependencies**: protobuf >=3.20.0
3. **New API**: Some method names have been updated for consistency
4. **Enhanced Features**: Full support for Vector Tile version 3 features

## Testing

Run the full test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=vector_tile_base --cov-report=html
```

