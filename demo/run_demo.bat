@echo off

pushd %~dp0

set TEST_FILE=test_data.m

echo #####################
echo ## Initial content ##
echo #####################
type %TEST_FILE%
echo.
echo.
echo ######################
echo ## Modified content ##
echo ######################
python -m regexp_replacer --debug %~dp0rules\main.md %TEST_FILE%

popd
