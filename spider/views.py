import os
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article

# Create your views here.
# 首先我们写好抓取网页的函数
from django.utils.crypto import random
from datetime import datetime
import time

# 简书爬文章 http://www.jianshu.com/c/8c92f845cd4d 绘画
from mysite import settings

address='http://www.jianshu.com'

def spider(request):
    return render(request,'spider/spider.html.')

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return "ERROR"

def get_article(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    litagList = soup.find('ul', {'class': 'note-list'}).find_all('li')

    contents = []
    for litag in litagList:
        content = {}
        try:
            aobj = litag.find('a',{'class': 'title'})
            content['title'] = aobj.text.strip()
            content['url'] = aobj['href']
            content['content'] = getContent(address + aobj['href'])
            content['abstract'] = litag.find('p',{'class': 'abstract'}).text
            content['author'] = litag.find('div',{'class': 'name'}).find('a', {'class': 'blue-link'}).text
            contents.append(content)
        except:
            print('出了点小问题')
            break
    return contents

# 获取文章
def getContent(url):
    html = get_html(url)
    # html = '<!DOCTYPE html> <!--[if IE 6]><html class="ie lt-ie8"><![endif]--> <!--[if IE 7]><html class="ie lt-ie8"><![endif]--> <!--[if IE 8]><html class="ie ie8"><![endif]--> <!--[if IE 9]><html class="ie ie9"><![endif]--> <!--[if !IE]><!--> <html> <!--<![endif]-->  <head>   <meta charset="utf-8">   <meta http-equiv="X-UA-Compatible" content="IE=Edge">   <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">    <!-- Start of Baidu Transcode -->   <meta http-equiv="Cache-Control" content="no-siteapp" />   <meta http-equiv="Cache-Control" content="no-transform" />   <meta name="applicable-device" content="pc,mobile">   <meta name="MobileOptimized" content="width"/>   <meta name="HandheldFriendly" content="true"/>   <meta name="mobile-agent" content="format=html5;url=http://www.jianshu.com/p/a88c174098d2">   <!-- End of Baidu Transcode -->      <meta name="description"  content="坦白地承认，目前正说明处于人生最为动荡迷茫的时期，与其任由自己惶惶然不如进行一场关于独处的修炼，一场手绘修炼。 #修炼第一章，小猫名叫haru。">    <meta name="360-site-verification" content="604a14b53c6b871206001285921e81d8" />   <meta property="wb:webmaster" content="294ec9de89e7fadb" />   <meta property="qc:admins" content="104102651453316562112116375" />   <meta property="qc:admins" content="11635613706305617" />   <meta property="qc:admins" content="1163561616621163056375" />   <meta name="google-site-verification" content="cV4-qkUJZR6gmFeajx_UyPe47GW9vY6cnCrYtCHYNh4" />   <meta name="google-site-verification" content="HF7lfF8YEGs1qtCE-kPml8Z469e2RHhGajy6JPVy5XI" />   <meta http-equiv="mobile-agent" content="format=html5; url=http://www.jianshu.com/p/a88c174098d2">    <!-- Apple -->   <meta name="apple-mobile-web-app-title" content="简书">      <!--  Meta for Smart App Banner -->   <meta name="apple-itunes-app" content="app-id=888237539, app-argument=jianshu://notes/18751496">   <!-- End -->    <!--  Meta for Twitter Card -->   <meta content="summary" property="twitter:card">   <meta content="@jianshucom" property="twitter:site">   <meta content="水彩猫" property="twitter:title">   <meta content="坦白地承认，目前正说明处于人生最为动荡迷茫的时期，与其任由自己惶惶然不如进行一场关于独处的修炼，一场手绘修炼。 #修炼第一章，小猫名叫haru。" property="twitter:description">   <meta content="http://www.jianshu.com/p/a88c174098d2" property="twitter:url">   <!-- End -->    <!--  Meta for OpenGraph -->   <meta property="fb:app_id" content="865829053512461">   <meta property="og:site_name" content="简书">   <meta property="og:title" content="水彩猫">   <meta property="og:type" content="article">   <meta property="og:url" content="http://www.jianshu.com/p/a88c174098d2">   <meta property="og:description" content="坦白地承认，目前正说明处于人生最为动荡迷茫的时期，与其任由自己惶惶然不如进行一场关于独处的修炼，一场手绘修炼。 #修炼第一章，小猫名叫haru。">   <!-- End -->    <!--  Meta for Facebook Applinks -->   <meta property="al:ios:url" content="jianshu://notes/18751496" />   <meta property="al:ios:app_store_id" content="888237539" />   <meta property="al:ios:app_name" content="简书" />    <meta property="al:android:url" content="jianshu://notes/18751496" />   <meta property="al:android:package" content="com.jianshu.haruki" />   <meta property="al:android:app_name" content="简书" />   <!-- End -->       <title>水彩猫 - 简书</title>    <meta name="csrf-param" content="authenticity_token" /> <meta name="csrf-token" content="EMJVgIPfzO/dvydstqga7E4W40/KVyxL7d4HyjKIfUyGxODCgc9jdW/mfVdTuTM7PIokdc5WE4Ee5xR6dOVz6w==" />    <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web-b6ffb2ef57d077ea3cf8.css" />     <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-319cd8f71e179151094e.css" />    <link href="//cdn2.jianshu.io/assets/favicons/favicon-03411b154a430b85d807b4366489c21122fb983a38f3d7ca926f882e6367b13e.ico" rel="icon">       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/57-a6f1f1ee62ace44f6dc2f6a08575abd3c3b163288881c78dd8d75247682a4b27.png" sizes="57x57" />       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/72-fb9834bcfce738fd7b9c5e31363e79443e09a81a8e931170b58bc815387c1562.png" sizes="72x72" />       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/76-49d88e539ff2489475d603994988d871219141ecaa0b1a7a9a1914f4fe3182d6.png" sizes="76x76" />       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/114-24252fe693524ed3a9d0905e49bff3cbd0228f25a320aa09053c2ebb4955de97.png" sizes="114x114" />       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/120-1bb7371f5e87f93ce780a5f1a05ff1b176828ee0d1d130e768575918a2e05834.png" sizes="120x120" />       <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/152-bf209460fc1c17bfd3e2b84c8e758bc11ca3e570fd411c3bbd84149b97453b99.png" sizes="152x152" />    <!-- Start of 访问统计 -->   <script>   (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){   (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),   m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)   })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');    ga(\'create\', \'UA-35169517-1\', \'auto\');   ga(\'send\', \'pageview\'); </script>  <script>   var _hmt = _hmt || [];   (function() {     var hm = document.createElement("script");     hm.src = "//hm.baidu.com/hm.js?0c0e9d9b1e7d617b3e6842e85b9fb068";     var s = document.getElementsByTagName("script")[0];     s.parentNode.insertBefore(hm, s);   })(); </script>    <!-- End of 访问统计 --> </head>    <body lang="zh-CN" class="reader-song-font">     <!-- 全局顶部导航栏 --> <nav class="navbar navbar-default navbar-fixed-top" role="navigation">   <div class="width-limit">     <!-- 左上方 Logo -->     <a class="logo" href="/"><img src="//cdn2.jianshu.io/assets/web/logo-58fd04f6f0de908401aa561cda6a0688.png" alt="Logo" /></a>      <!-- 右上角 -->       <!-- 未登录显示登录/注册/写文章 -->       <a class="btn write-btn" target="_blank" href="/writer#/">         <i class="iconfont ic-write"></i>写文章 </a>      <a class="btn sign-up" href="/sign_up">注册</a>       <a class="btn log-in" href="/sign_in">登录</a>      <!-- 如果用户登录，显示下拉菜单 -->      <div id="view-mode-ctrl">     </div>     <div class="container">       <div class="navbar-header">         <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menu" aria-expanded="false">           <span class="icon-bar"></span>           <span class="icon-bar"></span>           <span class="icon-bar"></span>         </button>       </div>       <div class="collapse navbar-collapse" id="menu">         <ul class="nav navbar-nav">             <li class="">               <a href="/">                 <span class="menu-text">首页</span><i class="iconfont ic-navigation-discover menu-icon"></i> </a>            </li>             <li class="">               <a class="app-download-btn" href="/apps"><span class="menu-text">下载App</span><i class="iconfont ic-navigation-download menu-icon"></i></a>             </li>           <li class="search">             <form target="_blank" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />               <input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" />               <a class="search-btn" href="javascript:void(null)"><i class="iconfont ic-search"></i></a> </form>          </li>         </ul>       </div>     </div>   </div> </nav>      <div class="note">   <div class="post">     <div class="article">         <h1 class="title">水彩猫</h1>          <!-- 作者区域 -->         <div class="author">           <a class="avatar" href="/u/cb069f2908da">             <img src="//upload.jianshu.io/users/upload_avatars/7960276/e89d74d9-3f7e-4164-8577-e41ce26f404e?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" /> </a>          <div class="info">             <span class="name"><a href="/u/cb069f2908da">花架与花</a></span>             <!-- 关注用户按钮 -->             <div props-data-classes="user-follow-button-header" data-author-follow-button></div>             <!-- 文章数据信息 -->             <div class="meta">               <!-- 如果文章更新时间大于发布时间，那么使用 tooltip 显示更新时间 -->                 <span class="publish-time">2017.10.24 14:23</span>               <span class="wordage">字数 67</span>             </div>           </div>           <!-- 如果是当前作者，加入编辑按钮 -->         </div>         <!-- -->          <!-- 文章内容 -->         <div data-note-content class="show-content">           <p>坦白地承认，目前正说明处于人生最为动荡迷茫的时期，与其任由自己惶惶然不如进行一场关于独处的修炼，一场手绘修炼。<br></p><p>#修炼第一章，小猫名叫haru。</p><div class="image-package"> <img src="//upload-images.jianshu.io/upload_images/7960276-f2f63821e5fd5ea5.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"><br><div class="image-caption">图片发自简书App</div> </div>         </div>         <!--  -->          <div class="show-foot">           <a class="notebook" href="/nb/16605344">             <i class="iconfont ic-search-notebook"></i>             <span>日记本</span> </a>          <div class="copyright" data-toggle="tooltip" data-html="true" data-original-title="转载请联系作者获得授权，并标注“简书作者”。">             © 著作权归作者所有           </div>           <div class="modal-wrap" data-report-note>             <a id="report-modal">举报文章</a>           </div>         </div>     </div>      <!-- 文章底部作者信息 -->       <div class="follow-detail">         <div class="info">           <a class="avatar" href="/u/cb069f2908da">             <img src="//upload.jianshu.io/users/upload_avatars/7960276/e89d74d9-3f7e-4164-8577-e41ce26f404e?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" /> </a>          <div props-data-classes="user-follow-button-footer" data-author-follow-button></div>           <a class="title" href="/u/cb069f2908da">花架与花</a>                   </div>       </div>        <div class="support-author"></div>      <div class="meta-bottom">       <div class="btn like-group"></div>       <div class="share-group">         <a class="share-circle" data-action="weixin-share" data-toggle="tooltip" data-original-title="分享到微信">           <i class="iconfont ic-wechat"></i>         </a>         <a class="share-circle" data-action="weibo-share" data-toggle="tooltip" href="javascript:void((function(s,d,e,r,l,p,t,z,c){var%20f=&#39;http://v.t.sina.com.cn/share/share.php?appkey=1881139527&#39;,u=z||d.location,p=[&#39;&amp;url=&#39;,e(u),&#39;&amp;title=&#39;,e(t||d.title),&#39;&amp;source=&#39;,e(r),&#39;&amp;sourceUrl=&#39;,e(l),&#39;&amp;content=&#39;,c||&#39;gb2312&#39;,&#39;&amp;pic=&#39;,e(p||&#39;&#39;)].join(&#39;&#39;);function%20a(){if(!window.open([f,p].join(&#39;&#39;),&#39;mb&#39;,[&#39;toolbar=0,status=0,resizable=1,width=440,height=430,left=&#39;,(s.width-440)/2,&#39;,top=&#39;,(s.height-430)/2].join(&#39;&#39;)))u.href=[f,p].join(&#39;&#39;);};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();})(screen,document,encodeURIComponent,&#39;&#39;,&#39;&#39;,&#39;http://cwb.assets.jianshu.io/notes/images/18751496/weibo/image_0a19c655fca5.jpg&#39;, &#39;推荐 花架与花 的文章《水彩猫》（ 分享自 @简书 ）&#39;,&#39;http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=weibo&#39;,&#39;页面编码gb2312|utf-8默认gb2312&#39;));" data-original-title="分享到微博">           <i class="iconfont ic-weibo"></i>         </a>           <a class="share-circle" data-toggle="tooltip" href="http://cwb.assets.jianshu.io/notes/images/18751496/weibo/image_0a19c655fca5.jpg" target="_blank" data-original-title="下载长微博图片">             <i class="iconfont ic-picture"></i>           </a>         <a class="share-circle more-share" tabindex="0" data-toggle="popover" data-placement="top" data-html="true" data-trigger="focus" href="javascript:void(0);" data-content=\'           <ul class="share-list">             <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=&#39;+e(&#39;http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=qzone&#39;)+&#39;&amp;title=&#39;+e(&#39;推荐 花架与花 的文章《水彩猫》&#39;),x=function(){if(!window.open(r,&#39;qzone&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-zone"></i><span>分享到QQ空间</span></a></li>             <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://twitter.com/share?url=&#39;+e(&#39;http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=twitter&#39;)+&#39;&amp;text=&#39;+e(&#39;推荐 花架与花 的文章《水彩猫》（ 分享自 @jianshucom ）&#39;)+&#39;&amp;related=&#39;+e(&#39;jianshucom&#39;),x=function(){if(!window.open(r,&#39;twitter&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-twitter"></i><span>分享到Twitter</span></a></li>             <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://www.facebook.com/dialog/share?app_id=483126645039390&amp;display=popup&amp;href=http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=facebook&#39;,x=function(){if(!window.open(r,&#39;facebook&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-facebook"></i><span>分享到Facebook</span></a></li>             <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://plus.google.com/share?url=&#39;+e(&#39;http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=google_plus&#39;),x=function(){if(!window.open(r,&#39;google_plus&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-google"></i><span>分享到Google+</span></a></li>             <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,s1=window.getSelection,s2=d.getSelection,s3=d.selection,s=s1?s1():s2?s2():s3?s3.createRange().text:&#39;&#39;,r=&#39;http://www.douban.com/recommend/?url=&#39;+e(&#39;http://www.jianshu.com/p/a88c174098d2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=douban&#39;)+&#39;&amp;title=&#39;+e(&#39;水彩猫&#39;)+&#39;&amp;sel=&#39;+e(s)+&#39;&amp;v=1&#39;,x=function(){if(!window.open(r,&#39;douban&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r+&#39;&amp;r=1&#39;};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})()"><i class="social-icon-sprite social-icon-douban"></i><span>分享到豆瓣</span></a></li>           </ul>         \'>更多分享</a>       </div>     </div>     <div id="vue_comment"></div>   </div>    <div class="vue-side-tool"></div> </div> <div class="note-bottom">   <div class="js-included-collections"></div>   <div data-vcomp="recommended-notes" data-lazy="1.5" data-note-id="18751496"></div> </div>      <script type="application/json" data-name="page-data">{"user_signed_in":false,"locale":"zh-CN","os":"other","read_mode":null,"read_font":null,"note_show":{"is_author":false,"is_following_author":false,"is_liked_note":false,"follow_state":0,"uuid":"771802ae-e4d0-4957-8dce-0dd04bc6a6b4"},"note":{"id":18751496,"slug":"a88c174098d2","user_id":7960276,"notebook_id":16605344,"commentable":true,"likes_count":0,"views_count":1,"public_wordage":67,"comments_count":0,"total_rewards_count":0,"is_author":false,"author":{"nickname":"花架与花","total_wordage":280,"followers_count":1,"total_likes_count":0}}}</script>         <script src="//cdn2.jianshu.io/assets/babel-polyfill-676833c6a4d68573b4c3.js" crossorigin="anonymous"></script>     <script src="//cdn2.jianshu.io/assets/web-base-f6535fa31c6f7630fbc1.js" crossorigin="anonymous"></script> <script src="//cdn2.jianshu.io/assets/web-66284f91873440622caf.js" crossorigin="anonymous"></script>         <script src="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-53cd167a1d5d33cd05fd.js" crossorigin="anonymous"></script>     <script>   (function(){       var bp = document.createElement(\'script\');       var curProtocol = window.location.protocol.split(\':\')[0];       if (curProtocol === \'https\') {           bp.src = \'https://zz.bdstatic.com/linksubmit/push.js\';       }       else {           bp.src = \'http://push.zhanzhang.baidu.com/push.js\';       }       var s = document.getElementsByTagName("script")[0];       s.parentNode.insertBefore(bp, s);   })(); </script>    </body> </html> '
    soup = BeautifulSoup(html, 'lxml')
    divObj = soup.find('div', {'class': 'show-content'})
    imagelist = divObj.find_all('div',{'class': 'image-package'})
    currtime = time.localtime()
    # 创建保存图片的目录
    dirname = time.strftime("%Y%m%d", currtime)
    realPath = settings.BASE_DIR + os.sep + 'common_static' + os.sep + 'images'+ os.sep  + 'jianshu'+ os.sep + dirname
    path = os.altsep + 'common_static' + os.altsep + 'images'+ os.altsep  + 'jianshu'+ os.altsep + dirname

    mkdir(realPath)
    imageprefix = time.strftime("%Y%m%d%H%M%S", currtime)

    for divimage in imagelist:
        image = divimage.find('img')
        imagesrc = image['src']
        imagedata = requests.get('http:'+ imagesrc).content
        imagename = imageprefix + str(random.randint(101, 999))+'.png'
        with open(realPath + os.sep + imagename, 'wb') as f:
            f.write(imagedata)
            f.flush()
            f.close()
        image['src'] = path + os.altsep + imagename
        del image['data-original-src']

    return str(divObj)

def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.makedirs(path)

# 保存数据
def save(contents):
    for content in contents:
        b = Article()
        b.cateid = 1
        b.catename='绘画'
        b.title = content['title']
        b.content = content['content']
        b.url = content['url']
        b.author= content['author']
        b.abstract = content['abstract']
        b.pubtime = datetime.utcnow()
        b.status = 0
        b.save()

# 生成静态页
def createStaticHtml(content):
    print(content)

def spiderJanshu(request):
    url = 'http://www.jianshu.com/c/8c92f845cd4d'
    json = {}
    try:
        # 抓取内容
        contents = get_article(url)
        # 保存到数据库
        save(contents)
        # 静态页面
        json = {'num': contents.__len__()}
    except:
        json = {'num': 0}

    return HttpResponse(json, content_type='application/json')