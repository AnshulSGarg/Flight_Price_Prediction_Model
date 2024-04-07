from flask import Flask, render_template, request
import pickle
import pandas

flight_df = pickle.load(open('book.pkl','rb'))
# recommend_dict = pickle.load(open('recommend.pkl','rb'))
book_list = list(recommend_dict.keys())
app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(book_df['Book-Title'].values),
                           image=list(book_df['Image-URL -M'].values),
                           Author=list(book_df['Book-Author'].values),
                           Year=list(book_df['Year-Of-Publication'].values),
                           Publisher=list(book_df['Publisher'].values),
                           Book_Rating=list(book_df['Book-Rating'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    # book_list = list(recommend_dict.keys())
    return render_template('recommend.html', book_list=book_list)

@app.route('/recommend_books', methods=['post'])
def recommend():
    # book_list = list(recommend_dict.keys())
    # print(book_list)
    user_input = request.form.get('user_input')
    print(user_input)
    print(recommend_dict[user_input]['book_title_list'])
    return render_template('recommend.html',
                           selected_book = user_input,
                            book_list=book_list,
                            book_title_list=recommend_dict[user_input]['book_title_list'],
                            Author_list = recommend_dict[user_input]['Author_list'],
                            publisher_list = recommend_dict[user_input]['publisher_list'],
                            year_list = recommend_dict[user_input]['year_list'],
                            image_list = recommend_dict[user_input]['image_list']
                           )

if _name_ == '_main_':
    app.run(debug=True)