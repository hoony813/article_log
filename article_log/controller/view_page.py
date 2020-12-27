from flask import render_template, request, redirect, session, current_app, flash, jsonify
from flask_login import login_required, current_user
import requests
from bs4 import BeautifulSoup

from article_log.article_log_blueprint import article_log_blueprint
from article_log.model.database import dao
from article_log.article_log_logger import Log
from article_log.model.article import Article


@article_log_blueprint.route('/article-view',methods=['GET','POST'])
@login_required
def article_view():

    if request.method == 'POST':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url = request.form['url']
        comment = request.form['comment']
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'lxml')

        image_url = soup.select_one('meta[property="og:image"]')['content']
        title = soup.select_one('meta[property="og:title"]')['content']
        description = soup.select_one('meta[property="og:description"]')['content']
        try:
            article = Article(user_id= current_user.id, article_title=title, article_url=url, article_src=image_url,article_description=description,comment=comment)
            dao.add(article)
            dao.commit()
        except Exception as e:
            error = "DB error occurs : " + str(e)
            dao.rollback()
            print(error)
            return jsonify({'result':'fail'})
        else:
            return jsonify({'result':'success'})
    return render_template('article_view.html')


@article_log_blueprint.route('/article-post',methods=['GET','POST'])
def get_my_article():
    try:

        articles = dao.query(Article).filter_by(user_id=current_user.id).all()
        ## print(current_user.__dir__())
        docs = []
        '''
        let url = cards[i]['url'];
                    let comment = cards[i]['comment'];
                    let title = cards[i]['title'];
                    let image = cards[i]['image'];
                    let desc = cards[i]['desc'];
        '''
        for a in articles:
            doc = dict()
            doc.update({'url':a.article_url,'comment':a.comment,'title':a.article_title,'image':a.article_src,'desc':a.article_description})
            docs.append(doc.copy())
    except:
        return jsonify({'result':'fail'})
    else:
        return jsonify({'result':'success','articles':docs})
