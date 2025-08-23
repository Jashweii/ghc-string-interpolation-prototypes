{-
To see output streamed, run with:

stack build --no-run-benchmarks :builders && \
  $(stack path --dist-dir)/build/builders/builders

https://github.com/commercialhaskell/stack/issues/1908
-}

import Criterion.Main
import Gen (testCases)

main :: IO ()
main =
  defaultMain
    [ bench label $ nf f ()
    | (alg, depth, len, f) <- testCases
    , let label = alg ++ "/depth=" ++ show depth ++ "/length=" ++ show len
    ]
