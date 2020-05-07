from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name = "Stranger"):
   page_setup = {
      'title': 'Seattle',
      'name': name, 
   }
   posts = [
      {
         'title': 'Why I love living in Seattle',
         'author': 'Jeff Bezos',
         'slug': 'The reasons that Seattle is AMAZING. I live here and loooove it.',
         'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti dolore suscipit fuga veritatis est reiciendis, inventore voluptas quidem pariatur illum cupiditate nostrum accusamus numquam. Excepturi, possimus ullam. Enim, quas aut?
Omnis cum dolores similique corrupti, amet aspernatur perferendis quos exercitationem alias reprehenderit iure delectus enim et ab commodi iste in, nemo facere illo accusantium tenetur nulla? At illo nihil quaerat.
Ea, ad consectetur tenetur totam accusantium doloribus quisquam veniam natus at perferendis. Pariatur tempora illum eligendi qui hic aspernatur, quia suscipit cupiditate eum corrupti dolores, fugiat rem. Voluptatem, laboriosam cum?
Ipsa quis fugit dolores dicta officiis incidunt, nisi dolorum excepturi! Illo asperiores iure eum, aliquam eligendi est minima libero vitae harum obcaecati id architecto ea quae ex tempore. Modi, praesentium.
Reiciendis sed dignissimos suscipit fugit quibusdam optio doloribus, quae quos obcaecati alias dolorum tenetur ullam, magnam, incidunt omnis quidem culpa natus quod cumque aut nisi minus molestias quaerat a. Libero!
In neque eum delectus adipisci, possimus ipsam veritatis quaerat incidunt recusandae voluptatum vel, ipsa nemo, quo natus facilis quisquam accusantium. Neque fugiat rem sapiente vero debitis in maiores, aliquid ratione!
Beatae non omnis quos, molestiae tempore harum quibusdam error delectus fugiat doloribus reiciendis quia dolor earum voluptatem aperiam iusto eligendi, perferendis praesentium impedit aliquid sit consequatur culpa. Dolor, voluptas ipsam?'''
      },
      {
         'title': 'Why Seattle is just the worst!',
         'author': 'Neal Stephenson',
         'slug': 'The reasons that Seattle is terrible. I live here and hate it.',
         'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti dolore suscipit fuga veritatis est reiciendis, inventore voluptas quidem pariatur illum cupiditate nostrum accusamus numquam. Excepturi, possimus ullam. Enim, quas aut?
Omnis cum dolores similique corrupti, amet aspernatur perferendis quos exercitationem alias reprehenderit iure delectus enim et ab commodi iste in, nemo facere illo accusantium tenetur nulla? At illo nihil quaerat.
Ea, ad consectetur tenetur totam accusantium doloribus quisquam veniam natus at perferendis. Pariatur tempora illum eligendi qui hic aspernatur, quia suscipit cupiditate eum corrupti dolores, fugiat rem. Voluptatem, laboriosam cum?
Ipsa quis fugit dolores dicta officiis incidunt, nisi dolorum excepturi! Illo asperiores iure eum, aliquam eligendi est minima libero vitae harum obcaecati id architecto ea quae ex tempore. Modi, praesentium.
Reiciendis sed dignissimos suscipit fugit quibusdam optio doloribus, quae quos obcaecati alias dolorum tenetur ullam, magnam, incidunt omnis quidem culpa natus quod cumque aut nisi minus molestias quaerat a. Libero!
In neque eum delectus adipisci, possimus ipsam veritatis quaerat incidunt recusandae voluptatum vel, ipsa nemo, quo natus facilis quisquam accusantium. Neque fugiat rem sapiente vero debitis in maiores, aliquid ratione!
Beatae non omnis quos, molestiae tempore harum quibusdam error delectus fugiat doloribus reiciendis quia dolor earum voluptatem aperiam iusto eligendi, perferendis praesentium impedit aliquid sit consequatur culpa. Dolor, voluptas ipsam?'''
      }
   ]
   verbose = None
   if name != "Stranger":
      verbose = True 
   
   return render_template('landing.html', page_setup=page_setup, posts=posts, verbose = verbose)

@app.route('/post')
def post():
   return render_template('post.html')