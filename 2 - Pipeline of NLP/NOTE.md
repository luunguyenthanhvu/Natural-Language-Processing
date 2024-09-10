# Quy trình xử lý văn bản (text pipeline) trong xử lý ngôn ngữ tự nhiên (NLP)
  1. Thu thập/Dữ liệu thu nhận
  2. Dọn dẹp văn bản
  3. Tiền xử lý
  4. Kỹ thuật đặc trưng
  5. Mô hình hóa
  6. Đánh giá
  7. Triển khai
  8. Giám sát

# NLP Pipeline: Tiền xử lý
  - Tiền xử lý văn bản có nghĩa là đưa văn bản của bạn vào một dạng có thể dự đoán và phân tích được cho nhiệm vụ của bạn.
  - Các kỹ thuật tiền xử lý văn bản bao gồm:
    + **Chuyển đổi thành chữ thường (Lowercasing)**: Chuyển tất cả các ký tự trong văn bản thành chữ thường để giảm thiểu sự khác biệt giữa các từ viết hoa và viết thường.
    + **Phân tách từ (Tokenization)**: Tách văn bản thành các đơn vị nhỏ hơn như từ hoặc cụm từ, để dễ dàng phân tích.
    + **Phân đoạn câu (Sentence Segmentation)**: Chia văn bản thành các câu riêng biệt, giúp phân tích cấu trúc câu và ngữ nghĩa.
    + **Cắt giảm từ (Stemming)**: Cắt bớt các hậu tố của từ để đưa từ về gốc của nó, ví dụ như biến "running" thành "run".
    + **Lemmatization**: Chuyển các từ về dạng cơ bản hoặc gốc của chúng dựa trên ngữ cảnh, ví dụ như "better" thành "good".
    + **Gán nhãn từ loại (POS tagging)**: Xác định loại từ (danh từ, động từ, tính từ, v.v.) cho mỗi từ trong văn bản, giúp hiểu ngữ pháp và chức năng của từ trong câu.
   
# Feature Engineering 
  1. **Quá trình sử dụng kiến thức miền dữ liệu để tạo ra các đặc trưng** giúp các thuật toán học máy hoạt động hiệu quả hơn.
  2. **Chuyển đổi các đặc điểm của văn bản thành định dạng số** mà các thuật toán học máy có thể hiểu và xử lý.
  3. Một số phương pháp để chuyển đổi dữ liệu văn bản thành định dạng số bao gồm:
       - ***Word Embeddings***: Đại diện từ vựng dưới dạng các vector số, thường sử dụng các kỹ thuật như Word2Vec hoặc GloVe để học mối quan hệ giữa các từ trong không gian vector.
       - ***CountVectorizer***: Phương pháp biến văn bản thành ma trận số lượng từ, đếm số lần xuất hiện của mỗi từ trong văn bản.
       - ***TF-IDF Vectorizer***: Phương pháp biến văn bản thành ma trận số với trọng số TF-IDF (Term Frequency-Inverse Document Frequency) để phản ánh tầm quan trọng của từ trong tài liệu so với toàn bộ tập hợp tài liệu.

# Thu Thập Dữ Liệu

## Tạo 1 Scrapy Project
Để tạo một dự án Scrapy, sử dụng lệnh sau:

```bash
scrapy startproject <project_name>
myproject/
    scrapy.cfg            # File cấu hình của Scrapy
    myproject/            # Thư mục chứa các thành phần của dự án
        __init__.py
        items.py          # Định nghĩa các item mà bạn muốn thu thập
        middlewares.py    # Định nghĩa các middleware cho dự án
        pipelines.py      # Định nghĩa các pipeline để xử lý dữ liệu
        settings.py       # File cấu hình của dự án
        spiders/          # Chứa các spider
            __init__.py
```
## Điều Hướng vào Thư Mục Dự Án
Sau khi tạo xong dự án, điều hướng vào thư mục dự án bằng lệnh: `cd <project_name>`

## Chạy Spider
Để chạy một spider và thu thập dữ liệu, sử dụng lệnh: `scrapy crawl <project_name>`

     
