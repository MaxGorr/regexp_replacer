@echo off

pushd %~dp0

set TEST_FILE=test.m

echo #####################
echo ## Initial content ##
echo #####################
type %TEST_FILE%
echo.
echo.
echo ######################
echo ## Modified content ##
echo ######################
python ..\rer_engine.py --debug sample_rules.rules %TEST_FILE%

popd
