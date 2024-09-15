# Khởi tạo một mô hình Word2Vec từ thư viện gensim để tạo ra các word embeddings

- <b> Khởi tạo: </b> `model = gensim.models.word2vec(window=10, size=100, min_count=2, sg=1)`
- Mô tả code:
    1. ` window=10 `
        + <b> Ý nghĩa: </b>  Đây là số lượng từ ngữ xung quanh (trong ngữ cảnh) mà mô hình sẽ xem xét cho mỗi từ đích.
        + <b> Chi tiết: </b> Với giá trị `window=10`, mô hình sẽ xem xét các từ trong phạm vi 10 từ xung quanh (cả trước và sau) từ đích để học cách chúng có liên quan với nhau. Ví dụ, nếu từ đích là "apple" thì mô hình sẽ nhìn vào 10 từ trước và sau từ "apple" để học ngữ cảnh.
    2. ` size=100 `
        + <b> Ý nghĩa: </b>  Đây là kích thước của các vector embedding, tức là mỗi từ sẽ được biểu diễn bằng một vector có 100 chiều.
        + <b> Chi tiết: </b> Vector 100 chiều này sẽ chứa các thông tin về mối liên quan của từ với các từ khác, dựa trên ngữ cảnh mà nó xuất hiện. Giá trị 100 là một kích thước phổ biến cho word embeddings, mặc dù bạn có thể tùy chỉnh giá trị này cho phù hợp với bài toán.
    3. ` min_count=2 `
        + <b> Ý nghĩa: </b> Đây là số lần xuất hiện tối thiểu của một từ trong tập dữ liệu để nó được mô hình học.
        + <b> Chi tiết: </b> Nếu một từ xuất hiện ít hơn 2 lần trong toàn bộ tập dữ liệu, nó sẽ bị bỏ qua. Điều này giúp giảm bớt việc huấn luyện với các từ hiếm hoặc lỗi chính tả, vì chúng có thể không cung cấp nhiều thông tin có giá trị cho mô hình.
    4. ` sg=1 `
        + <b> Ý nghĩa: </b> Đây là tham số quyết định sử dụng kiến trúc Skip-Gram hoặc CBOW (Continuous Bag of Words).
            - ` sg=1: ` Sử dụng mô hình Skip-Gram (dự đoán từ xung quanh dựa trên từ hiện tại).
            - ` sg=0: ` Sử dụng mô hình CBOW (dự đoán từ hiện tại dựa trên các từ xung quanh).
        + <b> Chi tiết: </b> ` sg=1 ` cho biết bạn đang sử dụng Skip-Gram. Với Skip-Gram, mô hình sẽ dự đoán các từ trong ngữ cảnh của từ hiện tại, tức là từ hiện tại (từ đích) sẽ được sử dụng để dự đoán các từ xung quanh nó trong cửa sổ ngữ cảnh.
    
