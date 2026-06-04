import pytest
from dataloader import CSVDataLoader


@pytest.fixture
def loader():
    return CSVDataLoader('Deliverable/sample.csv')

def test_loads_data(loader):
    loader.load()
    assert loader.data is not None


def test_validate(loader):
    with pytest.raises(ValueError):
        loader.validate()

    result = loader.load().validate()
    assert result is loader

def test_sample_returns_first_n_lines(loader):
    result = loader.load().sample(2)
    assert result == [
 "PassengerId,Survived,Pclass,Name,",
 "1,0,3,\"Braund, Mr. Owen Harris \""
]

def test_sample_return_large_n_lines(loader):
    result = loader.load().sample(100)
    assert len(result) == 6

def test_sample_loader(loader):
    with pytest.raises(ValueError):
        loader.sample(0)


def test_sample_case_zero(loader):
    result = loader.load().sample(0)
    assert result == []

def test_train_test_length(loader):
    train,test = loader.load().split(0.8)
    assert len(train) == 4
    assert len(test) == 1
    assert len(train) + len(test) == 5

def test_split_zero_ratio(loader):
    result = train, test = loader.load().split(0)
    assert len(train) == 0
    assert len(test) == 5

def test_stats_row_column(loader):
    stats = loader.load().stats()
    assert stats['rows'] == 6
    assert stats['columns'] == 5