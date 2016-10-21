@echo off

pushd %~dp0

type test.m | python ..\rer_engine.py sample_rules.rules

popd
