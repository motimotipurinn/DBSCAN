# DBSCAN

![sample](https://user-images.githubusercontent.com/69905754/222192468-e92c451e-3e9b-40c1-b944-71bd5130ff9b.png)

大昔にDBSCANで遊んでたの見つけたので放流するだけ

DBSCANとはクラスタリングしながらノイズ除去できるもので、アルゴリズムとしては点と半径εを定めて、その円の中にminPts個以上の隣接点を持つ点をcore点、1~minPts個の隣接点をreachable点、0個のoutlier点にわけてreachable点を各core点のクラスタに配属していくという行動をとります

aaaa~dddd.txtはそれぞれ別のデータセットです
