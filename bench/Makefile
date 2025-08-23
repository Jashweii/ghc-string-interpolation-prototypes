BENCH_NAME = "interpolation-bench"

Gen.hs: generate.py
	./generate.py

.PHONY: run
run: Main.hs Gen.hs
	# Don't use stack bench to see streamed output
	# https://github.com/commercialhaskell/stack/issues/1908
	stack build --no-run-benchmarks :$(BENCH_NAME)
	$$(stack path --project-root)/$$(stack path --dist-dir)/build/$(BENCH_NAME)/$(BENCH_NAME)
