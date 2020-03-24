#!/bin/env python3
import json


class TCObj():
    json = ()
    keys = ()

    def __init__(self, json_obj):
        for key in self.keys:
            if key in json_obj:
                setattr(self, key, json_obj[key])
            else:
                setattr(self, key, None)
        self.json = json_obj


class TCAppObj(TCObj):
    keys = (
        'client_id',
        'name',
        'owner_user_id'
    )


class TCCategoryObj(TCObj):
    keys = (
        'id',
        'name',
        'sub_categories'
    )

    def __init__(self, json_obj):
        super().__init__(json_obj)
        self.sub_categories = [
            TCSubCategoryObj(subcat) for subcat in self.sub_categories
        ]


class TCCommentObj(TCObj):
    keys = (
        'id',
        'message',
        'from_user',
        'created'
    )

    def __init__(self, json_obj):
        super().__init__(json_obj)
        self.from_user = TCUserObj(self.from_user)


class TCMovieObj(TCObj):
    keys = (
        'id',
        'user_id',
        'title',
        'subtitle',
        'last_owner_comment',
        'category',
        'link',
        'is_live',
        'is_recorded',
        'comment_count',
        'large_thumbnail',
        'small_thumbnail',
        'country',
        'duration',
        'created',
        'is_collabo',
        'is_protected',
        'max_view_count',
        'current_view_count',
        'total_view_count',
        'hls_url'
    )


class TCSubCategoryObj(TCObj):
    keys = (
        'id',
        'name',
        'count'
    )


class TCSupporterUserObj(TCObj):
    keys = (
        'id',
        'screen_id',
        'name',
        'image',
        'profile',
        'level',
        'last_movie_id',
        'is_live',
        'supporter_count',
        'supporting_count',
        'point',
        'total_point',
        'created'  # deprecated
    )


class TCUserObj(TCObj):
    keys = (
        'id',
        'screen_id',
        'name',
        'image',
        'profile',
        'level',
        'last_movie_id',
        'is_live',
        'supporter_count',  # deprecated
        'supporting_count',  # deprecated
        'created'           # deprecated
    )


class TCWebHookObj(TCObj):
    keys = (
        'user_id',
        'event'
    )


class TCErrorObj(TCObj):
    keys = (
        'code',
        'message',
        'details'
    )
