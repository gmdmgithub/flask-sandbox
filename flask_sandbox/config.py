
#lets add some posted data (simply not from db)
posts = [
    {
        'author': 'John Doe',
        'title': 'My best friend',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-01-15'
    },
    {
        'author': 'Janet Jackson',
        'title': 'My brother',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-02-15'
    },
    {
        'author': 'John Kennedy',
        'title': 'My country',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-03-15'
    }
]

home_p ={
    'active':'home',
    'menu': True,
    'title' : 'Home page'
}
about_p ={
    'active':'about',
    'menu': True,
    'title' : 'About page'
}

register_p = {
    'active':'registration',
    'menu': False,
    'title': 'Registration page'
}

login_p = {
    'active':'login',
    'menu': False,
    'title': 'Login page'
}
account_p = {
    'active':'account',
    'menu': True,
    'title': 'Account page'
}