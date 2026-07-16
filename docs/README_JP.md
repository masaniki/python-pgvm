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

PGLはCSV(Comma Separated Value)の形で記述されます。

PGLは2つの構文しか持ちません。それはCOPY文とIF文です。

## 参照について

nodeの参照は、全てroot_nodeから行います。

pointer graph内でのnode間の移動は、`edge_label`を使って行われます。

`path`とは、edge_labelを`/`区切りしたものです。

↓ EBNFによるpathの定義。

`<path> ::= <edge_label>(/<edge_label>)*`

## COPY文

COPY文は、edgeを動かすための文です。

COPY文はBNF likeな表現で次の様に表されます。

`cp, <path1>, <path2>, <row_index>`

`<path1>`には、編集するedgeもしくは、新しく生成するedgeを指定するためのpathを指定します。

`<path2>`には、edgeを編集した後の状態を指定するためのpathを指定します。

- 特殊なpath `delete`
  
  `<path1>=既知のedge`　かつ　`<path2>=delete`　の時、`<path1>`の末尾のedgeを削除します。

- 特殊なpath `new`
  
  `<path1>=未知のedge`　かつ　`<path2>=new`　の時、`<path1>`の位置に新しいnodeを生成します。

`<row_index>`には、COPY文を実行した後のjump先の行番号を記述します。

## IF文

IF文は、2つのnodeを比較して、その結果に応じて次の命令の変更するための文です。

IF文はBNF likeな表現で次の様に表される。

`if, <path1>, <path2>, <row_index1>, <row_index2>`

`<path1>`には、比較するnodeを指定するためのpathを記述します。

`<path2>`には、比較するnodeを指定するためのpathを記述します。

- 特殊なpath `delete`
  
  `<path2>`に`delete`を指定すると、`<path1>`が存在しない時に`<row_index1>`へjumpし(trueと同じ挙動)、存在する時に`<row_index2>`へjumpします。

`<row_index1>`には、`<path1>`と`<path2>`の比較結果がtrueだった場合のjump先の行番号を記述します。

`<row_index2>`には、`<path1>`と`<path2>`の比較結果がfalseだった場合のjump先の行番号を記述します。

## 例

- nodeの参照のsample program.

- edgeの終点の付け替えのsample program.

- nodeの生成のsample program.

- nodeの削除のsample program.


