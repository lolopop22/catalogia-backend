from catalogia.domain.film import Film


def test_film_model_init():
    film = Film(
        poster = "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg",
        title = "The Untouchables",
        runtime = 119,
        directors = ["Brian De Palma"],
        producers = ["Raymond Hartwick", "Art Linson"],
        cast = ["Kevin Costner", "Sean Connery", "Charles Martin Smith"],
        synopsis = "After building an empire with bootleg alcohol, legendary crime boss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"
    )

    assert film.poster == "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg"
    assert film.title == "The Untouchables"
    assert film.runtime == 119
    assert film.directors == ["Brian De Palma"]
    assert film.producers == ["Raymond Hartwick", "Art Linson"]
    assert film.cast == ["Kevin Costner", "Sean Connery", "Charles Martin Smith"]
    assert film.synopsis ==  "After building an empire with bootleg alcohol, legendary crime boss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"


def test_film_from_dict():
    init_dict = {
        "poster": "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg",
        "title": "The Untouchables",
        "runtime": 119,
        "directors": ["Brian De Palma"],
        "producers": ["Raymond Hartwick", "Art Linson"],
        "cast": ["Kevin Costner", "Sean Connery", "Charles Martin Smith"],
        "synopsis": "After building an empire with bootleg alcohol, legendary crime boss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"
    }

    film = Film.from_dict(init_dict)
    
    assert film.poster == "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg"
    assert film.title == "The Untouchables"
    assert film.runtime == 119
    assert film.directors == ["Brian De Palma"]
    assert film.producers == ["Raymond Hartwick", "Art Linson"]
    assert film.cast == ["Kevin Costner", "Sean Connery", "Charles Martin Smith"]
    assert film.synopsis ==  "After building an empire with bootleg alcohol, legendary crime boss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"


def test_film_to_dict():
    init_dict = {
        "poster": "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg",
        "title": "The Untouchables",
        "runtime": 119,
        "directors": ["Brian De Palma"],
        "producers": ["Raymond Hartwick", "Art Linson"],
        "cast": ["Kevin Costner", "Sean Connery", "Charles Martin Smith"],
        "synopsis": "After building an empire with bootleg alcohol, legendary crime bo`ss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"
    }

    film = Film.from_dict(init_dict)

    assert film.to_dict() == init_dict


def test_film_model_comparison():
    init_dict = {
        "poster": "https://m.media-amazon.com/images/M/MV5BYTVjYWJmMWQtYWU4Ni00MWY3LWI2YmMtNTI5MDE0MWVmMmEzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg",
        "title": "The Untouchables",
        "runtime": 119,
        "directors": ["Brian De Palma"],
        "producers": ["Raymond Hartwick", "Art Linson"],
        "cast": ["Kevin Costner", "Sean Connery", "Charles Martin Smith"],
        "synopsis": "After building an empire with bootleg alcohol, legendary crime bo`ss Al Capone rules Chicago with an iron fist. Though Prohibition Agent Eliot Ness attempts to take Capone down"
    }

    film1 = Film.from_dict(init_dict)
    film2 = Film.from_dict(init_dict)

    assert film1 == film2

