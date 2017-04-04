from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello_world_2_tmpl.html', hello_string='Witamy')
    
@app.route("/about")
def about():
    about_info = {
        'name': 'Onufry',
        'surname': 'Zagłoba',
        'age': 'tyle ile trzeba',
    }
    return render_template('about_tmpl.html', about_info=about_info)
    
@app.route('/handle_post', methods=['POST'])
def handle_post():
    data = request.get_json()
    print('Received \ndata: `{}`\ntype(data): `{}`'.format(data, type(data)))
    return 'dane otrzymane'
    
    
@app.route("/simple_path/<sample_variable>")
def simple_path(sample_variable):
    print(sample_variable)
    print(type(sample_variable))
    print(app.url_map)
    return '\n\r'.join((
        "Hello Flask World!",
        'my_path: `{}`'.format(sample_variable),
        'type(my_path): `{}`'.format(type(sample_variable)),
        'id(my_path): `{}`'.format(id(sample_variable)),
    ))
    
@app.route("/simple_path_tmpl/<sample_variable>")
def simple_path_tmpl(sample_variable):
    print(sample_variable)
    print(type(sample_variable))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=sample_variable,
        my_type=type(sample_variable),
        my_id=id(sample_variable),
    )
    
@app.route("/simple_path_int/<int:sample_variable>")
def simple_path_int(sample_variable):
    print(sample_variable)
    print(type(sample_variable))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=sample_variable,
        my_type=type(sample_variable),
        my_id=id(sample_variable),
    )
    
@app.route("/path/<path:my_path>")
def path_all(my_path):
    print(my_path)
    print(type(my_path))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=my_path,
        my_type=type(my_path),
        my_id=id(my_path),
    )

if __name__ == "__main__":
    app.run()
