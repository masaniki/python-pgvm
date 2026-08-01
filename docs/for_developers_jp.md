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

## 前回からの変更点

- [x] generate node文の追加。
- [x] generate edge文の追加。
- [x] switch edge文の追加。
- [x] delete文の追加。
- [x] programの可視化用の関数の追加。
- [x] root nodeはimport時に指定する。
- [x] new記号やdelete記号の削除。
- [ ] test caseの追加。

## Ideas

次、実装する可能性があるideaを記述する。

- 引数を複数にできるようにする。
- rootに複数のfileを接続する。
- 未達度が大きいpathでも一気に生成できるようにする？
- PGRuntimeErrorの追加。
- Turing machineとの比較。

# Others
