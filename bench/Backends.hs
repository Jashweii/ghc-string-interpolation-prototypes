{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE TypeFamilyDependencies #-}

module Backends where

import Data.Monoid (Endo (..))

class Interpolate1 a where
  interpolate1 :: a -> String
instance Interpolate1 String where
  interpolate1 = id
instance Interpolate1 Int where
  interpolate1 = show

class Buildable s where
  type Builder s = b | b -> s
  toBuilder :: s -> Builder s
  fromBuilder :: Builder s -> s

instance Buildable String where
  type Builder String = Endo String
  toBuilder s = Endo (s <>)
  {-# INLINE toBuilder #-}
  fromBuilder (Endo f) = f []
  {-# INLINE fromBuilder #-}

{-# RULES "fromBuilder/toBuilder" forall x. fromBuilder (toBuilder x) = x #-}
{-# RULES "toBuilder/fromBuilder" forall x. toBuilder (fromBuilder x) = x #-}

class Interpolate2 a s where
  interpolate2 :: a -> Builder s
instance Interpolate2 String String where
  interpolate2 = toBuilder
instance Interpolate2 Int String where
  interpolate2 = toBuilder . show
