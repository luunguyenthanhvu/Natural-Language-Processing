# Continuous Bag of Words (CBOW)

## Mô tả:
  - Continuous Bag of Words (CBOW) là một mô hình học từ trong xử lý ngôn ngữ tự nhiên (NLP) được sử dụng trong việc học nhúng từ (word embeddings). Đây là một trong hai mô hình chính trong Word2Vec, mô hình còn lại là Skip-gram.

## Cách Hoạt Động của CBOW
  1. Mục Tiêu:
      - CBOW dự đoán từ mục tiêu (từ trung tâm) dựa trên các từ ngữ cảnh xung quanh nó.
  2. Cấu Trúc Mô Hình:
      - <b> Input: </b> Một tập hợp các từ xung quanh từ mục tiêu (context words).
      - <b> Output: </b> Từ mục tiêu (target word) mà mô hình dự đoán dựa trên ngữ cảnh.
  3. Quá Trình Đào Tạo:
      - Trong quá trình đào tạo, mô hình nhận vào các từ ngữ cảnh (từ xung quanh từ mục tiêu) và cố gắng dự đoán từ mục tiêu.
      - Ví dụ, nếu chúng ta có một câu "The cat sat on the mat" và từ mục tiêu là "sat" với các từ ngữ cảnh là "The", "cat", "on", "the", "mat", mô hình CBOW sẽ cố gắng dự đoán từ "sat" từ các từ ngữ cảnh này.  
  4. Kiến Trúc Mô Hình:
      - <b> Input Layer: </b> Các từ ngữ cảnh được mã hóa thành các vector one-hot và sau đó chuyển thành các vector nhúng (embedding vectors) qua ma trận nhúng từ (embedding matrix).
      - <b> Hidden Layer: </b> Các vector nhúng được cộng lại và chia trung bình để tạo thành một vector ngữ cảnh đại diện cho từ mục tiêu.
      - <b> Output Layer: </b> Vector ngữ cảnh được nhân với ma trận trọng số để dự đoán xác suất của từ mục tiêu.
  5. Đào Tạo:
      - CBOW sử dụng hàm mất mát (loss function) như hàm mất mát phân loại (cross-entropy loss) để tối ưu hóa các trọng số của ma trận nhúng từ và ma trận trọng số đầu ra.

## Lợi Ích của CBOW
  - <b> Hiệu Suất: </b> CBOW thường hoạt động tốt hơn khi có dữ liệu lớn và khi các từ ngữ cảnh có số lượng lớn.
  - <b> Đào Tạo Nhanh: </b> Mô hình CBOW có thể đào tạo nhanh hơn trên các tập dữ liệu lớn so với mô hình Skip-gram trong một số tình huống.

## So Sánh với Skip-gram
  - <b> Skip-gram: </b> Dự đoán các từ ngữ cảnh từ một từ mục tiêu. Mô hình này thường hiệu quả hơn khi làm việc với dữ liệu không đầy đủ hoặc khi từ vựng rất lớn.
  - <b> CBOW: </b> Dự đoán từ mục tiêu từ các từ ngữ cảnh. Mô hình này thường phù hợp hơn khi có nhiều dữ liệu huấn luyện và từ ngữ cảnh được cung cấp đầy đủ.
