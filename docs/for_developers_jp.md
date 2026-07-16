# For Developers

開発者向けのmessageを記述する。

## Deployment

### build

`Python -m build .`

### upload

test PyPIへのupload.

`twine upload -r testpypi "dist/*"`

PyPIへのupload

`twine upload "dist/*"`

## Testing

testの仕方を記述する。

## Branchs

branch戦略を記述する。

### `master`

現在公開中のbranch。

### `develop`

非破壊的commitのみが許されているbranch。

masterへmergeする。

### `feat/*`

破壊的commitができるbranch。

developへmergeする。

merge後は削除。

## Next To Do

- [ ] 引数を複数にできるようにする。

## Ideas

次、実装する可能性があるideaを記述する。

- 未達度が大きいpathでも一気に生成できるようにする？

# Others
