# Word Embedding

<details>
  <summary>
  <b> 1. Khái niệm </b>
  </summary>

  - Word Embedding là tên gọi chung của các mô hình ngôn ngữ và các phương pháp học theo đặc trưng trong Xử lý ngôn ngữ tự nhiên(NLP), ở đó các từ hoặc cụm từ được ánh xạ sang các vector số (thường là số thực). Đây là một công cụ đóng vai trò quan trọng đối với hầu hết các thuật toán, kiến trúc Machine Learning, Deep Learning trong việc xử lý Input ở dạng text, do chúng chỉ có thể hiểu được Input ở dạng là số, từ đó mới thực hiện các công việc phân loại, hồi quy,vv…
</details>

<details>
  <summary>
  <b> 2. Các loại Word Embedding </b>
  </summary>

  - Word Embedding được phân chủ yếu thành 2 loại:
      + [Frequency-based Embedding](frequency_based_embedding.md).
      + [Prediction-based embedding](prediction_based_embedding.md).

</details>

<details>
  <summary>
  <b> 3. Một chút so sánh giữa Word2vec và GloVe </b>
  </summary>

  - Về bản chất, rõ ràng Word2vec và GloVe khác nhau do thuộc 2 loại Embedding khác nhau nhưng đều bắt nguồn từ Context Window, Word2vec sử dụng Context Window để tạo ra các tập train cho mạng neuron còn GloVe sử dụng nó để tạo ra Co-occurrence Matrix. Để ý kĩ một chút, ta thấy rằng GloVe mang tính “toàn cục” hơn là Word2vec vì GloVe tính toán xác suất từ dựa trên toàn bộ tập dữ liệu còn Word2vec học dựa trên các ngữ cảnh đơn lẻ, cũng chính vì lý do này mà GloVe có trội hơn Word2vec cũng như vài mô hình khác trong một số task về ngữ nghĩa, nhận dạng thực thể có gắn tên,vv… Ngoài ra, GloVe có độ ổn định trung bình tốt hơn Word2vec, độ ổn định ở đây chính là độ biến thiên của kết quả giữa hai lần ta thực hiện việc học với cùng một điều kiện xác định (cùng bộ dữ liệu, cùng tham số, cùng điều kiện phần cứng,…).

</details>


<details>
  <summary>
  <b> 4. Ứng dụng </b>
  </summary>

  Word Embedding tạo ra các vector từ mà dựa vào đó ta có thể áp dụng chúng để thực hiện các thao tác về ngữ nghĩa như là tìm từ đồng nghĩa, trái nghĩa,… Ngoài ra, chúng cũng là nguồn tài nguyên cho các hệ thống Machine Learning, Deep Learning nhằm thực hiện các mục đích cao hơn như là các hệ thống máy dịch, phân tích cảm xúc dựa trên ngôn từ,vv…
</details>
