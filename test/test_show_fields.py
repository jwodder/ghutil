from ghutil.showing import show_fields

INPUT = {
    "name": "Foo",
    "alive": True,
    "parent": {
        "name": "Bar",
        "disappointed": True,
    },
    "children": [
        {
            "name": "Baz",
            "disappointing": False,
            "resources": {
                "wood": 4626,
                "gold": 43,
                "stone": 0,
                "sheep": 3,
                "food": 8327,
            },
        },
        {
            "name": "Quux",
            "disappointing": True,
            "resources": {
                "wood": 0,
                "gold": 0,
                "stone": 0,
                "sheep": 0,
                "food": 95028841,
            },
        },
        {
            "name": "Glarch",
            "disappointing": False,
            "resources": {
                "wood": 0,
                "gold": 9716,
                "stone": 93,
                "sheep": 99375,
                "food": 1,
            },
        },
    ],
    "resources": {
        "wood": 314,
        "gold": 1592,
        "stone": 6535,
        "sheep": 89793238,
        "food": 0,
    },
    "home": None,
}

def test_select():
    assert show_fields(('name', 'alive', 'parent'), INPUT) == {
        "name": "Foo",
        "alive": True,
        "parent": {
            "name": "Bar",
            "disappointed": True,
        },
    }

def test_select_nonexistent():
    assert show_fields(('name', 'alive', 'parent', 'nonexistent'), INPUT) == {
        "name": "Foo",
        "alive": True,
        "parent": {
            "name": "Bar",
            "disappointed": True,
        },
    }

def test_select_subfield():
    assert show_fields(('name', ('parent', 'name')), INPUT) == {
        "name": "Foo",
        "parent": "Bar",
    }

def test_select_list_subfield():
    assert show_fields(('name', ('children', 'name')), INPUT) == {
        "name": "Foo",
        "children": ["Baz", "Quux", "Glarch"],
    }

def test_select_null():
    assert show_fields(('name', 'home'), INPUT) == {
        "name": "Foo",
        "home": None,
    }

def test_select_null_subfield():
    assert show_fields(('name', ('home', 'name')), INPUT) == {
        "name": "Foo",
        "home": None,
    }

def test_select_callable():
    assert show_fields(
        ('name', ('resources', lambda r: {k:v for k,v in r.items() if v})),
        INPUT,
    ) == {
        "name": "Foo",
        "resources": {
            "wood": 314,
            "gold": 1592,
            "stone": 6535,
            "sheep": 89793238,
        },
    }

def test_select_recursive():
    assert show_fields(
        ('name', ('children', ('name', ('resources', 'food')))),
        INPUT,
    ) == {
        "name": "Foo",
        "children": [
            {
                "name": "Baz",
                "resources": 8327,
            },
            {
                "name": "Quux",
                "resources": 95028841,
            },
            {
                "name": "Glarch",
                "resources": 1,
            },
        ]
    }
