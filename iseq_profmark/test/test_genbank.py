from pathlib import Path

from assertpy import assert_that, contents_of
from iseq_profmark import GenBank, example_filepath


def test_genbank_gb(tmp_path: Path):
    gb = example_filepath("CP041245.1.gb")
    acc = "CP041245.1"
    output = tmp_path / f"{acc}.gb"
    GenBank.download(acc, "gb", output)
    assert_that(contents_of(gb)).is_equal_to(contents_of(output))


def test_genbank_fasta(tmp_path: Path):
    fasta = example_filepath("CP041245.1.fasta")
    acc = "CP041245.1"
    output = tmp_path / f"{acc}.fasta"
    GenBank.download(acc, "fasta", output)
    assert_that(contents_of(fasta)).is_equal_to(contents_of(output))
