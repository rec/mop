# Hack script just to "show my work".

ROOT=/development/mop

PY_ROOT=$ROOT/gen/py
PROTO_ROOT=$ROOT/src/proto

mkdir -p "$PY_ROOT"

protoc \
 --proto_path="$PROTO_ROOT" \
 --python_out="$PY_ROOT" \
 "$PROTO_ROOT/"*/*/*.proto