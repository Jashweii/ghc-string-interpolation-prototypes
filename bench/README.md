Run benchmarks

```shell
make -C bench run
```

We use `generate.py` to generate `Gen.hs` with desugared interpolations, to more precisely simulate what will be compiled, instead of dynamically building with `foldr`.
