# 概要

- pointer grpahとは、全てのnodeがpointerで構成されているgraphです。
- node間は名前付き有向edgeで結びついています。
- pointer graph languageとは、pointer grpahを操作するための形式言語です。
- 本libraryは、pointer graphをpointer graph languageで動かすための仮想的な機械を提供します。

# インストール方法

`pip install pgvm`

# 使い方

簡単な使用例を記述する。

# Pointer Graphについて

Pointer Graph.

# PGL(Pointer Graph Language)について

PGLは、pointer grpahを操作するための形式言語です。

PGLはCSV(Comma Separated Value)のような形で記述されます。

PGLは2つの構文しか持ちません。それはCOPY文とIF文です。

## COPY文

COPY文は、edgeを動かすための文である。

COPY文はBNF likeな表現で次の様に表される。

`cp, <path1>, <path2>, <row_index>`

`<path1>`には、編集するedgeもしくは、新しく生成するedgeを指定するためのpathを指定する。

`<path2>`には、edgeを編集した後の状態を指定するためのpathを指定する。

- 特殊なpath `delete`
  
  `<path1>=既知のedge`　かつ　`<path2>=delete`　の時、`<path1>`の末尾のedgeを削除する。

- 特殊なpath `new`
  
  `<path1>=未知のedge`　かつ　`<path2>=new`　の時、`<path1>`の位置に新しいnodeを生成する。

`<row_index>`には、COPY文を実行した後のjump先の行番号を記述する。

## IF文

IF文は、2つのnodeを比較して、その結果に応じて次の命令の変更するための文である。

IF文はBNF likeな表現で次の様に表される。

`if, <path1>, <path2>, <row_index1>, <row_index2>`

`<path1>`には、比較するnodeを指定するためのpathを記述する。

`<path2>`には、比較するnodeを指定するためのpathを記述する。

- 特殊なpath `delete`
  
  `<path2>`に`delete`を指定すると、`<path1>`が存在しない時に`<row_index1>`へjumpし(trueと同じ挙動)、存在する時に`<row_index2>`へjumpする。

`<row_index1>`には、`<path1>`と`<path2>`の比較結果がtrueだった場合のjump先の行番号を記述する。

`<row_index2>`には、`<path1>`と`<path2>`の比較結果がfalseだった場合のjump先の行番号を記述する。

## 例

- nodeの参照のsample program.

- edgeの終点の付け替えのsample program.

- nodeの生成のsample program.

- nodeの削除のsample program.


## Next To Do

- [ ] to do things.

## Ideas

次、実装する可能性があるideaを記述する。

# Others


