# Tiền sử lý văn bản với NLTK

  - <b> Đọc văn bản:</b>`text = f.read()`  
  - <b> Tách câu thành các token: </b> `nltk.word_tokenize`
  - <b> Loại bỏ ký tự xuống dòng:</b> `text.replace("\n", " ")`
  - <b> Biến đổi về chữ thường: </b>`text.lower()`
  - <b> Gán Part-Of-Speech (POS) tags (nhãn từ loại): </b> `nltk.pos_tag`
      + sử dụng để gán Part-Of-Speech (POS) tags (nhãn từ loại) cho các từ trong một câu hoặc một đoạn văn bản. POS tags giúp xác định chức năng ngữ pháp của từng từ, chẳng hạn như danh từ, động từ, tính từ, trạng từ, v.v.
      + Ví dụ về các POS tags:
	  - NN: Danh từ chung (Noun)
	  - VB: Động từ gốc (Verb)
	  - JJ: Tính từ (Adjective)
	  - RB: Trạng từ (Adverb)
	  - PRP: Đại từ (Pronoun)
	  - Và nhiều nhãn khác... 
  - <b> Tách các câu:</b>
      + Từ một đoạn văn bản gồm nhiều câu thì thông qua bước này ta thu được các câu thành phần. Để nhận biết một câu đơn giản nhất là khi gặp dấu "." kết thúc câu, chúng ta hoàn toàn có thể sử dụng hàm split() trong python và tách câu mỗi khi gặp dấu ".". Tuy nhiên, không phải lúc nào dấu "." cũng là kết thúc câu, ví dụ trong tiếng anh, từ "Mr. Smith" thì nếu ta dùng cách trên để bóc tách các câu thì sẽ sai. Để có thể tách các câu chính xác thì việc sử dụng các thư viện hỗ trợ là biện pháp đơn giản nhất cụ thể là sử dụng hàm `nltk.sent_tokenize`.
      +   EX:
            ```bash
           sentence_list = nltk.sent_tokenize(raw_text)
            # Print some sentences
            for i in range(100, 110):
              print(sentence_list[i])
              print("-----")
            print("---------------------------------------")
            print(f"Number of sentences: {len(sentence_list)}")
            ```
      + Bên cạnh hàm để tách các câu thì thư viện NLTK cũng cung cấp hàm để tách các từ `nltk.word_tokenize`.
  - <b> Loại bỏ các kí tự đặc biệt (dấu câu): </b>
      + Trong các câu trong văn bản sẽ tồn tại nhiều dấu câu như ?, !, ", ;, ... trước khi xây dựng bộ từ vựng thì các kí tự này cũng cần được loại bỏ. Python đã định nghĩa các dấu câu trong `string.punctuation` tuy vào bài toán ta có thể thêm hoặc bớt các dấu này cho phù hợp.
      + EX:
          ```bash
          import string
          print("Punctuations: " + string.punctuation + "\n")
          sentence_list = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentence_list]
          
          for i in range(100, 110):
            print(sentence_list[i])
            print("-----")
          ```
      + Không chỉ dấu "," và "." trong câu đã được loại bỏ thì các dấu được định nghĩa trong `string.punctuation` cũng được bỏ đi. Ngoài ra ta có thể thêm bớt các dấu tùy theo mục đích.
  - <b> Loại bỏ stop-word: </b>
    + Stop words thường là các từ xuất hiện nhiều lần và không đóng góp nhiều vào ý nghĩa của câu, chúng sẽ đóng vai trò như nhiễu, trong tiếng Anh các từ này có thể kể đến như the, is, at, on, which, in, some, many hay trong tiếng Việt là các từ cái, các, cả,.... Các từ này thường sẽ được loại bỏ để giảm kích thước của bộ từ vựng. Trong thư viện NLTK có định nghĩa các stop words phổ biến trong tiếng Anh, tuy nhiên tùy thuộc vào mục đích, bài toàn mà ta sẽ thêm bớt các stop word cho phù hợp. Để sử dụng stop words của NLTK, trước tiên ta cần download bộ stop words `nltk.download('stopwords')`.
    + EX:
        ```bash
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        
        stop_word_list = set(stopwords.words('english'))
        print(stop_word_list, "\n")
        for i in range(len(sentence_list)):
          sentence_list[i] = " ".join([word for word in sentence_list[i].split() if word not in stop_word_list])
        
        for i in range(100, 110):
          print(sentence_list[i])
          print("-----")

        ```
  - <b> Loại bỏ các từ hiếm gặp: </b>
      + Bên cạnh stop words thì trong nhiều bài toán ta cũng cần phải loại bỏ các từ hiếm gặp, đặc biệt khi bộ dữ liệu lớn. Đây cũng là kĩ thuật mà ta cần cân nhắc trước khi sử dụng bởi loại bỏ các từ này có thể gây ra sự mất mát về ngữ nghĩa của câu, đặc biệt là với các bộ dữ liệu trung bình, nhỏ. Để loại bỏ các từ hiếm ta sẽ dùng Counter để đếm số lần xuất hiện của các từ và tìm ra các từ ít xuất hiện nhất, sau đó loại bỏ các từ này trong câu như đối với stop words.
      + EX:
          ```bash
          from collections import Counter
          # get word list
          word_list =list()
          for sentence in sentence_list:
            for word in sentence.split():
              word_list.append(word)
          word_counter = Counter(word_list)
          
          # for example, remove 10 rare words
          rare_word_list = set([word for (word, word_count) in word_counter.most_common()[:-10-1:-1]])
          print(rare_word_list)
          for i in range(len(sentence_list)):
            sentence_list[i] = " ".join([word for word in sentence_list[i].split() if word not in rare_word_list])
          ```
  - <b> Stemming & Lemmatization: </b>
    + Stemming là quá trình biến đổi các từ về dạng gốc của nó (ví dụ: connected, connection khi stemming thu được connect hay moved, move khi stemming thu được mov), lưu ý là stemming đơn giản là loại bỏ phần cuối của từ tuy nhiên dạng của từ thu được chưa chắc đã tồn tại trong tiếng Anh (như từ mov) (khá tệ!!). Thông thường kĩ thuật này được sử dụng để chuẩn hóa bộ từ vựng và ta cũng cần cân nhắc sử dụng theo bài toán đặt ra. Trong thư viện NLTK cũng có hỗ trợ thuật toán `Porter` để thực hiện nhiệm vụ này.
    + EX:
        ```bash
        from nltk.stem.porter import PorterStemmer
        
        stemmer = PorterStemmer()
        stemmed_sentence_list = []
        for i in range(len(sentence_list)):
          stemmed_sentence_list.append(" ".join([stemmer.stem(word) for word in sentence_list[i].split()]))
        
        for i in range(100, 110):
          print(stemmed_sentence_list[i])
          print("-----")

        ```
        Khi quan sát output, ta thấy một số từ như eruption -> erupt, astronomer -> astronom....
  
  - <b> Lemmatization </b>
      + Lemmatization về cơ bản là giống với stemming khi nó loại bỏ phần đuôi của từ để thu được gốc từ, tuy nhiên các gốc từ ở đây đều thực sự tốn tại chứ không như stemming (như ví dụ trên thì từ moved sau khi lemmatize sẽ thu được move). Trong thư viện NLTK sẽ sử dụng từ điển Wordnet để map theo các quy tắc (theo tính chất của từ, từ là danh từ, động từ, trạng từ hay tính từ). Sử dụng *part-of-speech tagging* `(nltk.pos_tag)` để thu được các tính chất của từ.
      + EX:
          ```bash
          from nltk.stem import WordNetLemmatizer
          from nltk.corpus import wordnet
          
          wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
          lemmatizer = WordNetLemmatizer()
          lemmatized_sentence_list = []
          for i in range(len(sentence_list)):
            pos_tagged_sentence = nltk.pos_tag(sentence_list[i].split())
            lemmatized_sentence_list.append(" ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_sentence]))
          
          for i in range(100, 110):
            print(lemmatized_sentence_list[i])
            print("-----")

          ```
    - <b> Loại bỏ các emoji: </b>
        + Đối với một số bài toán sử dụng dữ liệu là các văn bản từ những trang mạng xã hội như Twitter, Facebook,... thì việc loại bỏ các biểu tượng cảm xúc - emoji là vô cùng cần thiết. Để loại bỏ emoji ta sẽ sử dụng `regex, pattern` lấy từ repo này khá đầy đủ và hoạt động tốt.
        + EX:
            ```bash
            emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002500-\U00002BEF"  # chinese char
                            u"\U00002702-\U000027B0"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642"
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f"  # dingbats
                            u"\u3030"
                            "]+", flags=re.UNICODE)
            emoji_example = "😅 👠 😆 Without you by my side, 💓 😉 I am not complete. You have given me the best of love, 🎈 and I want to be by your side forever. Thank you for giving my life that direction it needed. 💋‍ Thank you for loving me unconditional. 💏"
                  print(emoji_pattern.sub(r'', emoji_example))

            ```
    - <b>Loại bỏ URL </b>
        + Khi crawl dữ liệu từ nhiều nguồn thì không thể tránh khỏi việc các dữ liệu này sẽ dính các đường dẫn URL khác nhau. Sử dụng regex để loại bỏ các URL.
        + EX:
            ```bash
            url_example = "You can read more about AI at https://viblo.asia/"
            url_pattern = re.compile(r'http\S+')
            print(url_pattern.sub(r'', url_example))

            ```

