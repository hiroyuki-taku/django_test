# django_test
Docker + Django + rest frameworkを試してみたサンプル。

# Dependency
`Dockerfile`、`requirements.txt`を参照のこと

# Setup

``` bash
$docker-compose build
$docker-compose up
```

mysqlを利用しているが、そちらはリポジトリに含めていない。  
別環境に持っていった際にはデータは存在しないので注意。

# References
Special Thanks

* [DockerでDjangoの開発環境を作成する（Quickstart: Compose and DjangoのMySQL版）](https://aoishi.hateblo.jp/entry/2017/11/05/153341)
* [【Django入門】REST FrameworkでAPIを作ってみよう](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
* [Django REST Frameworkを使って爆速でAPIを実装する](https://www.sejuku.net/blog/29189#REST_Framework)