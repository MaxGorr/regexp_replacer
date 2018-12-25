@pushd %~dp0

type test_data.m | python -m regexp_replacer -r %~dp0rules\main.md -s

@popd
