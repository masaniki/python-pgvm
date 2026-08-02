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

## deployment process

- feat/* branchで開発。
- 単体test合格。
- feat/*をdevelopにmerge.
- PyPIへupload.
- developをmasterにmerge.
- tagを書いて、remoteにpushする。
- gitHubでrelease noteを書く。

## 前回からの変更点

- [x] pathが存在しない時の、if文の処理の実装。(false側へ分岐する)
- [x] EditableGraph.visualizeProgram()に、行番号を追加した。

## Ideas

次、実装する可能性があるideaを記述する。

- 未達度が大きいpathでも一気に生成できるようにする？
- Turing machineとの比較。
- encoding関数とdecoding関数の実装。
- nodeのgarbage collection。
- node番号の重複回避の仕組み。

  graph fileの時は、nodeは文字列によって表現されるが、それをimportする時に、nodeに識別子となる番号を付与する。

# Others
