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

一般的に、graph構造と言えば、nodeに値を格納しているのが一般的です。

例えば、二分木であればnodeに整数値を持っています。

しかし、もし値を使わずに様々な概念を表現できるのであれば、文字や数値は必須ではありません。

このideaを検証するために作られたのが、このPointer Graphです。

Pointer Graphの各nodeは、node pointerの配列と、edgeの識別子の配列で構成されています。

この時の、edgeの識別子のことを`edge label`と呼びます。

`edge label`はただの文字列です。

`edge label`の数とnode pointerの数は同じになっており、`edge label`を指定することで、隣接するnodeへ遷移できます。(詳しくは参照の所へ)

binaryのcomputerが、数値や文字をbit列に変換するように、Pointer Grpahも数値や文字をgraph構造で表現し直す必要があります。

このように、私たちが普段扱っている概念をgraph構造に変換することを、`grpah encoding`と呼びます。

# PGL(Pointer Graph Language)について

PGLは、pointer grpahを操作するための形式言語です。

PGLは1行ずつ実行されるscript言語です。

PGLの各引数は、`,`で区切られており、CSV(Comma Separated Value)のような形で表現されます。

PGLの最初の引数はkeywordとなっており、そのkeywordによって命令を判断します。これをコマンドと呼びます。

命令は、 generate node(GN), generate edge(GE), switch edge(SE), delete(DEL), ifの5つです。

以下は、コマンドの使い分けの早見表です。

| コマンド名     | edgeが存在 | 終点のnodeが存在 |
| ---           | ---        | ---             |
| generate node | x          | x               |
| generate edge | x          | o               |
| switch edge   | o          | o               |


## 参照について

nodeの参照は、全てroot_nodeから行います。

pointer graph内でのnode間の移動は、`edge_label`を使って行われます。

`path`とは、edge_labelを`/`区切りしたものです。

↓ EBNFによるpathの定義。

`<path> ::= <edge_label>(/<edge_label>)*`

## generate node

generate nodeは、未知のnodeへの新しいedgeを生成します。形式表現は以下の通りです。

`gn, <path1>, <row_index>`

- `<path1>`
  
  新しく生成するnodeへのpathを指定する。

- `<row_index>`
  
  命令を実行した後のjump先の行番号を記述します。

## generate edge

generate edgeは、未知のnodeへの新しいedgeを生成します。形式表現は以下の通りです。

`ge, <path1>, <path2>, <row_index>`

- `<path1>`
  
  新しく生成するpathを指定する。

- `<path2>`
  
  edgeの新しい終点を指定する。既知のnodeを指定する。

- `<row_index>`
  
  命令を実行した後のjump先の行番号を記述します。

## switch edge

switch edgeは、既知のpathの終点を既知のnodeへ切り替える関数です。形式表現は以下の通りです。

`se, <path1>, <path2>, <row_index>`

- `<path1>`
  
  編集するedgeもしくは、新しく生成するedgeを指定するためのpathを指定します。

- `<path2>`

  edgeを編集した後の状態を指定するためのpathを指定します。

- `<row_index>`
  
  命令を実行した後のjump先の行番号を記述します。

## delete

delete文は、edgeを削除する命令です。形式表現は以下の通りです。

`del, <path1>, <row_index>`

- `<path1>`

  削除するedgeを指定する。

- `<row_index>`

  命令を実行した後のjump先の行番号を記述します。

## if

if文は、2つのnodeを比較して、その結果に応じて次の命令の変更するための文です。形式表現は以下の通りです。

`if, <path1>, <path2>, <row_index1>, <row_index2>`

- `<path1>`

  比較するnodeを指定するためのpathを記述します。

- `<path2>`

  比較するnodeを指定するためのpathを記述します。

  - 特殊なpath `delete`
  
    `<path2>`に`delete`を指定すると、`<path1>`が存在しない時に`<row_index1>`へjumpし(trueと同じ挙動)、存在する時に`<row_index2>`へjumpします。

- `<row_index1>`

  `<path1>`と`<path2>`の比較結果がtrueだった場合のjump先の行番号を記述します。

- `<row_index2>`

  `<path1>`と`<path2>`の比較結果がfalseだった場合のjump先の行番号を記述します。

## 例

- nodeの参照のsample program.

- edgeの終点の付け替えのsample program.

- nodeの生成のsample program.

- nodeの削除のsample program.


