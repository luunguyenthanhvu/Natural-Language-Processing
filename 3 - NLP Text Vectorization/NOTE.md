# Vector Hóa Văn Bản

### Vector hóa văn bản là một bước quan trọng trong xử lý ngôn ngữ tự nhiên (NLP), nơi dữ liệu văn bản được chuyển đổi thành các đại diện số mà các thuật toán học máy có thể sử dụng. Đây là cái nhìn tổng quan về các kỹ thuật vector hóa văn bản phổ biến:
<details>
  <summary>
  <b> 1. Bag of Words (BoW) </b>
  </summary>

  - <b> Khái Niệm: </b> Đại diện cho dữ liệu văn bản dưới dạng một tập hợp các số lượng từ.
  - <b> Quy Trình: </b>
      1. Tách văn bản thành các từ (token).
      2. Tạo một từ vựng gồm tất cả các từ duy nhất trong tập dữ liệu.
      3. Tạo một vector cho mỗi văn bản, trong đó mỗi phần tử của vector là số lượng xuất hiện của từ tương ứng trong văn bản đó.
</details>

<details>
  <summary>
  <b> 2. TF-IDF (Term Frequency-Inverse Document Frequency) </b>
  </summary>

  - <b> Khái Niệm: </b>  Cân nhắc tần suất xuất hiện của từ trong một tài liệu và tầm quan trọng của từ đó trong toàn bộ tập tài liệu.
  - <b> Quy Trình: </b>
      1. Tính tần suất từ (TF), tức là số lần từ xuất hiện trong tài liệu.
      2. Tính tần suất nghịch đảo tài liệu (IDF), phản ánh mức độ quan trọng của từ trong toàn bộ tập tài liệu.
      3. Tính TF-IDF bằng cách nhân TF với IDF cho mỗi từ.
</details>

<details>
  <summary>
  <b>  3. Word Embeddings </b>
  </summary>

  - <b> Khái Niệm: </b>  Đại diện từ bằng các vector số thực, nơi từ có nghĩa tương tự sẽ có các vector gần nhau trong không gian vector.
  - <b> Các Kỹ Thuật: </b>
      - ***Word2Vec:*** Sử dụng mô hình Skip-gram hoặc Continuous Bag of Words (CBOW) để học các vector từ.
      - ***GloVe (Global Vectors for Word Representation):*** Học các vector từ bằng cách phân tích ma trận đồng xuất hiện của từ trong tài liệu.
</details>

<details>
  <summary>
  <b>  4.  Sent2Vec / Sentence Embeddings </b>
  </summary>

  - <b> Khái Niệm: </b>  Đại diện cho toàn bộ câu hoặc đoạn văn bằng một vector số, không chỉ là từng từ riêng lẻ.
  - <b> Kỹ Thuật: </b>
      - ***Universal Sentence Encoder:*** Mô hình học máy học cách đại diện cho các câu bằng các vector số.
</details>

<details>
  <summary>
  <b>  5.  Transformers </b>
  </summary>

  - <b> Khái Niệm: </b>  Mô hình hiện đại như BERT và GPT có thể tạo ra các đại diện văn bản rất chính xác bằng cách sử dụng các lớp Attention để hiểu ngữ cảnh từ.
</details>


