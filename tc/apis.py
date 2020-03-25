#!/bin/env python3
from typing import List, Optional

from tc.auth import TCAuth, TCAppAuth, TCUserAuth
from tc.reqs import TCRequest, make_req


# User
def get_user_info(auth: TCAuth,
                  user_id: str) \
        -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/users/' + user_id)


def verify_credentials(auth: TCUserAuth) \
        -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/verify_credentials')


# Live Thumbnail
def get_live_thumbnail_image(auth: Optional[TCAuth],
                             user_id: str,
                             size: str = 'small',
                             position: str = 'latest'
                             ) \
        -> TCRequest:
    '''
    size: "large" or "small"
    position: "beginning" or "latest"
    '''
    return make_req(auth,
                    'GET',
                    '/users/%s/live/thumbnail' % user_id,
                    {'size': size,
                     'position': position})


# Movie
def get_movie_info(auth: TCAuth,
                   movie_id: int) \
        -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/movies/' + movie_id)


def get_movies_by_user(auth: TCAuth,
                       user_id: str,
                       offset: int = 0,
                       limit: int = 20,
                       slice_id: Optional[int] = None) \
        -> TCRequest:
    '''
    offset: min:0 max:1000
    limit: min:1 max:50
    slice_id: min:1
    '''
    args = {'limit': limit}
    if slice_id:
        args['slice_id'] = slice_id
    else:
        args['offset'] = offset
    return make_req(auth,
                    'GET',
                    '/users/%s/movies' % user_id,
                    args)


def get_current_live(auth: TCAuth,
                     user_id: str) \
        -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/users/%s/current_live' % user_id)


# Comment
def get_comments(auth: TCAuth,
                 movie_id: int,
                 offset: int = 0,
                 limit: int = 10,
                 slice_id: int = 1) \
        -> TCRequest:
    '''
    offset: min:0
    limit: min:1 max:50
    slice_id: min:1
    '''
    args = {'limit': limit}
    if slice_id:
        args['slice_id'] = slice_id
    else:
        args['offset'] = offset
    return make_req(auth,
                    'GET',
                    '/movies/%d/comments' % movie_id,
                    args)


def post_comment(auth: TCUserAuth,
                 movie_id: int,
                 comment: str,
                 sns: str = 'none') \
        -> TCRequest:
    '''
    comment: len:1~140
    sns: "reply", "normal" or "none"
    '''
    return make_req(auth,
                    'POST',
                    '/movies/%d/comments' % movie_id,
                    {'comment': comment,
                     'sns': sns})


def delete_comment(auth: TCUserAuth,
                   movie_id: int,
                   comment_id: str) \
        -> TCRequest:
    return make_req(auth,
                    'DELETE',
                    '/movies/%d/comments/%s' % (movie_id, comment_id))


# Supporter
def get_supporting_status(auth: TCAuth,
                          user_id: str,
                          target_user_id: str) \
        -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/users/%s/supporting_status' % user_id,
                    {'target_user_id': target_user_id})


def support_user(auth: TCUserAuth,
                 target_user_ids: List) \
        -> TCRequest:
    '''
    target_user_ids: list len:<20
    '''
    return make_req(auth,
                    'PUT',
                    '/support',
                    {'target_user_ids': target_user_ids})


def unsupport_user(auth: TCUserAuth,
                   target_user_ids: List) \
        -> TCRequest:
    '''
    target_user_ids: list len:<20
    '''
    return make_req(auth,
                    'PUT',
                    '/unsupport',
                    {'target_user_ids': target_user_ids})


def supporting_list(auth: TCAuth,
                    user_id: str,
                    offset: int = 0,
                    limit: int = 20) \
        -> TCRequest:
    '''
    offset: min:0
    limit: min:1 max:20
    '''
    return make_req(auth,
                    'GET',
                    '/users/%s/supporting' % user_id,
                    {'offset': offset,
                     'limit': limit
                     })


def supporter_list(auth: TCAuth,
                   user_id: str,
                   sort: str,
                   offset: int = 0,
                   limit: int = 20) \
        -> TCRequest:
    '''
    sort: "new" or "ranking"
    offset: min:0
    limit: min:1 max:20
    '''
    return make_req(auth,
                    'GET',
                    '/users/%s/supporters' % user_id,
                    {'offset': offset,
                     'limit': limit,
                     'sort': sort})


# Category
def get_categories(auth: TCAuth,
                   lang: str) \
        -> TCRequest:
    '''
    lang: "en" or "ja"
    '''
    return make_req(auth,
                    'GET',
                    '/categories',
                    {'lang': lang})


# Search
def search_users(auth: TCAuth,
                 words: str,
                 limit: int = 10,
                 lang: str = 'ja') \
        -> TCRequest:
    '''
    words: space separated words AND search
    limit: min:1 max:50
    lang: only "ja"
    '''
    return make_req(auth,
                    'GET',
                    '/search/users',
                    {'words': words,
                     'limit': limit,
                     'lang': lang})


def search_live_movies(auth: TCAuth,
                       type: str,
                       context: str = '',
                       limit: int = 10,
                       lang: str = 'ja') \
        -> TCRequest:
    '''
    limit: min:1 max:100
    type: "tag", "word", "category", "new" or "recommend"
    context: needed for type "tag" "word" and "category"
    lang: only "ja"
    '''
    return make_req(auth,
                    'GET',
                    '/search/lives',
                    {'limit': limit,
                     'type': type,
                     'context': context,
                     'lang': lang})


# WebHook
def get_webhook_list(auth: TCAppAuth,
                     limit: int = 50,
                     offset: int = 0,
                     user_id: Optional[str] = None) \
        -> TCRequest:
    '''
    limit: min:1 max:50
    offset: min:0
    these two only valid when no user_id specified
    '''
    if user_id:
        return make_req(auth, 'GET', '/webhooks',
                        {'user_id': user_id})
    else:
        return make_req(auth, 'GET', '/webhooks',
                        {'limit': limit, 'offset': offset})


def register_webhook(auth: TCAppAuth,
                     user_id: str,
                     events: List) \
        -> TCRequest:
    '''
    events: array, "livestart" and "liveend"
    '''
    return make_req(auth,
                    'POST',
                    '/webhooks',
                    {'user_id': user_id,
                     'events': events})


def delete_webhook(auth: TCAppAuth,
                   user_id: str,
                   events: List) \
        -> TCRequest:
    '''
    events: array, "livestart" and "liveend"
    '''
    return make_req(auth,
                    'DELETE',
                    '/webhooks',
                    {'user_id': user_id,
                     'events': events})


# Broadcasting
def get_rtmp_url(auth: TCUserAuth) -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/rtmp_url')


def get_webm_url(auth: TCUserAuth) -> TCRequest:
    return make_req(auth,
                    'GET',
                    '/webm_url')


# Realtime API
def ws_lives(auth: TCAuth) -> str:
    if isinstance(auth, TCAppAuth):
        auth: TCAppAuth
        return 'wss://%s:%s@realtime.twitcasting.tv/lives' % (auth.client_id, auth.client_secret)
    elif isinstance(auth, TCUserAuth):
        auth: TCUserAuth
        return 'wss://realtime.twitcasting.tv/lives?token=' + auth.access_token
    else:
        raise TypeError(
            'auth should be an instance of TCAppAuth or TCUserAuth')

