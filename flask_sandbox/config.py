# TODO - chcange to db
# DONE
#lets add some posted data (simply not from db) - 
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

#page parameters
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
    'menu': True,
    'title': 'Registration page'
}

login_p = {
    'active':'login',
    'menu': True,
    'title': 'Login page'
}
account_p = {
    'active':'account',
    'menu': True,
    'title': 'Account page'
}
new_post_p = {
    'active':'post',
    'menu': True,
    'title': 'Create/edit a post'
}
post_p = {
    'active': 'edit_post',
    'menu': True,
    'title':'Edit a post'
}
rest_request_p = {
    'active': 'rest_request',
    'menu': True,
    'title':'Request to reset the password'
}
rest_password_p = {
    'active': 'rest_request',
    'menu': True,
    'title':'Rreset the password'
}
# list pagination per page
pagin_per_page = 3