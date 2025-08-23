#!/usr/bin/env python3

from pathlib import Path

HERE = Path(__file__).absolute().parent
OUTPUT = HERE / "Gen.hs"

TEMPLATE = """
module Gen where

import qualified Data.String.Syntax.ImplicitBuilder as ImplicitBuilder
import qualified Data.String.Syntax.ImplicitOnlyString as ImplicitOnlyString

testCases :: [(String, Int, Int, () -> String)]
testCases =
  [ {test_cases}
  ]
""".strip("\n")

def main():
    test_cases = [
        gen_test_case(alg, depth, length)
        for alg in [
            "implicit-only-string",
            "implicit-builder",
        ]
        for (depth, length) in [
            *((0, n) for n in [1, 2, 3, 4, 5, 10, 50, 100]),
            # changing depth when length=1 doesn't seem to change runtime
            *((n, 2) for n in [1, 2, 3, 4, 5, 10]),
        ]
    ]
    OUTPUT.write_text(TEMPLATE.format(test_cases="\n  , ".join(test_cases)))

def gen_test_case(alg, depth, length):
    test_str = gen_test_str(alg, depth, length)
    return f'("{alg}", {depth}, {length}, \\_ -> {test_str})'

def gen_test_str(alg, depth, length):
    # don't use mempty for empty because we need to guide type inference if there aren't any string literals
    match alg:
        case "implicit-only-string":
            finalizer = ""
            empty = '""'
            interpolator = "ImplicitOnlyString.interpolate"
        case "implicit-builder":
            finalizer = "ImplicitBuilder.fromBuilder $ "
            empty = 'ImplicitBuilder.toBuilder ""'
            interpolator = "ImplicitBuilder.interpolate"

    """
    let s0 = s"${s1}${s1}..."
        s1 = s"${s2}${s2}..."
        ...
        sN = s"${x}${x}..."
        x = 123 :: Int
     in s0
    """
    vals = [
        f"s{n} = " + finalizer + " <> ".join(
            f"{interpolator} {"x" if n == depth else f"s{n + 1}"}"
            for _ in range(length)
        ) + f" <> {empty}"
        for n in range(depth + 1)
    ] + ["x = 123 :: Int"]
    return "let " + "; ".join(vals) + " in s0"

if __name__ == "__main__":
    main()
