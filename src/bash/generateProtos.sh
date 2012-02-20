# Hack script just to "show my work".

ROOT=/development/mop

JAVA_ROOT=$ROOT/gen/java
PY_ROOT=$ROOT/gen/py
PROTO_ROOT=$ROOT/src/proto

mkdir -p "$JAVA_ROOT" "$PY_ROOT"

protoc \
 --proto_path="$PROTO_ROOT" \
 --java_out="$JAVA_ROOT" \
 --python_out="$PY_ROOT" \
 "$PROTO_ROOT/"*/*/*.proto