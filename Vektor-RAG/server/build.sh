docker build \
--network=host \
--no-cache \
-t rag-framework:latest \
--target rag-framework \
-f Dockerfile \
.
