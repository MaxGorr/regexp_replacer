@pushd %~dp0

type test_data.m | python -m regexp_replacer %~dp0rules\main.md

@popd
