# WEB

1. 요청의 종류
   * get
   * post

# Dynamic Web

1. flask: python을 이용한 웹 프레임워크(django와 유사)

   1. set up

      * ```
        $ pip install Flask
        $ FLASK_APP=hello.py flask run
        ```

   2. FLASK_DEBUG=1 FLASK_APP=hello.py flask run:  변경사항 자동 저장

   3. ```
      if __name__ == '__main__': # 시작점??
          app.run(debug=True)
      ```

      * python hello.py로 실행 가능

      * ```
        __name__
        ```

   4. ```
      @app.route("/")
      def hello():
          return "Hello World!"
      ```

      * 주소 지정
      * @: decorator
      * app.route의 파라미터로 아래의 함수 사용

   5. ```
      def hello(func):
          print('hi hi')
          func() # --> bye()를 실행한 것과 동일
          print('hi hi')
      
      
      @hello
      def bye():
          print('bye bye')
      
      bye()
      ```

      * 실행결과: hi hi  \n bye bye  \n hi hi

   6. path variable: path variable과 parameter 일치 시켜야 한다

      * ```
        @app.route('/greeting/<string:name>')
        def greeting(name):
            return f'반갑습니다, {name}님'
        ```

      * ```
        @app.route('/cube/<int:num>')
        def cube(num):
            result = num ** 3
            return str(result) # 문자로 변환해주어야한다(현재 result는 int)
        ```

   7. ```
      <!--hi.html-->
      <body>
          <h1>반갑습니다!{{your_name}}</h1>
      </body>
      
      
      #hello.py
      @app.route('/hi/<string:name>')
      def hi(name):
          return render_template('hi.html', your_name=name)
      ```

      * render_template: html문서 실행 위해
      * 실행결과(localhost/hi/sky): 반갑습니다!sky

   8. ```
      <!--menu_list.html-->
      <body>
      	<!-- html문서에서 python 사용하기 -->
          {% for menu in menu_list %}
              <li>{{menu}}</li>
          {% endfor %}
      </body>
      
      #hello.py
      @app.route('/menu_list')
      def menu_list():
          menu = ['분식', '한식', '중식', '양식', '일식']
          return render_template('menu_list.html', menu_list=menu)
      ```

      * 실행결과: 

        분식

        한식

        중식

        양식

        일식

   9. flask에서는 파일명을 app.py로 만드는것을 권장한다

   10. ```
       <!-- send.html -->
       <body>
           <form action="/receive"> <!-- 요청을 보낼 곳 지정 -->
               <!-- 입력창 2개, 제출버튼 하나 -->
               <input type="text" name="user">
               <input type="text" name="message">
               <input type="submit">
           </form>
       </body>
       
       <!-- receive.html -->
       <body>
           <h1>Receive!</h1>
           <h2>From {{user}}: {{message}}</h2>
       </body>
       
       # app.py
       @app.route('/send')
       def send():
           return render_template('send.html')
       
       @app.route('/receive')
       def receive():
           # 주소를 통해 받아온 정보를 dictionary 형태로 request.args에 담는다(sky, hi 입력)
           # user: 'sky', message: 'hi'
           user = request.args.get('user') # --> 'sky'
           message = request.args.get('message') # --> 'hi'
           return render_template('receive.html', user=user, message=message)
       ```

       * /send web page에서 sky / hi를 입력하고, 제출버튼을 누르면 /recieve web page로 이동하며, 아래와 같이 화면에 나타난다

       * Receive!

         From sky : hi

2. Dictionary

   1. lunch = {'keys': 'values'}

   2. dict(): dictionary로 변환하는 메소드 ex. dict(중국집='02')

   3. dict item 추가

      lunch['분식집'] = '054-'

   4. dict value 가져오기

      * lunch = {'한식집': {'고갯마루': '02', '순남시래기': '031'

        }

      * lunch['한식집'] --> dict

      * lunch['한식집'] ['고갯마루'] --> '02'

   5. dict 내부 자료형

      * key: string, integer, float, boolean
      * value: 모든 자료형(list, dict....)

   6. dictionary 반복문 활용

      * ```
        lunch = {
            '한식집': '02-',
            '중식집' : '031-',
            '일식집' : '054-'
        }
        ```

      * ```
        # 4-1. 기본
        for key in lunch:
            print(key) # key
            print(lunch[key]) # value
        
        # 4-2. key 기본
        for key in lunch.keys(): # --> ['한식집', ...]
            print(key)
        
        # 4-3. value 반복
        for value in lunch.values(): # --> ['02-', '031-', ...]
            print(value)
        
        # 4-4. key, value 반복
        for key, value in lunch.items(): # --> [('한식집, '02-'), ...]
            print(key)
            print(value)
        ```

   7. ```
      winner list를 만드는 두가지 방법
      1.
      winner = []
      for n in range(1, 7):
          winner.append(lotto[f'drwtNo{n}'])
      
      2.    
      # list comprehension
      a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
      ```