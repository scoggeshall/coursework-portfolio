"""Negative tests use only a disposable fixture beneath this repository."""
import shutil, unittest
from validate_site import ROOT, validate

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.target=ROOT/'docs/test-work'
        if self.target.exists(): raise RuntimeError('Refusing to overwrite existing test-work')
        shutil.copytree(ROOT/'site',self.target)
    def tearDown(self):
        assert self.target.resolve()==(ROOT/'docs/test-work').resolve() and self.target.resolve().is_relative_to(ROOT)
        shutil.rmtree(self.target)
    def reject(self,name,data,expected=None):
        p=self.target/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data)
        with self.assertRaisesRegex(ValueError, expected or 'manifest differs'):
            validate(self.target, sealed=expected is None)
    def test_private_extensions(self):
        for ext in ['docx','pptx','pdf','db','sqlite','sqlite3','sql','py','zip','csv']:
            with self.subTest(ext=ext):
                self.reject('private.'+ext,b'private fixture','Prohibited file/path')
                (self.target/('private.'+ext)).unlink()
    def test_disguised_pdf(self): self.reject('assets/disguised.png',b'%PDF-1.7','Prohibited binary signature')
    def test_archive_path(self): self.reject('archive/old.html',b'<p>Old</p>','Prohibited file/path')
    def test_pii(self): self.reject('privacy.html',b'<p>Student-ID: TEST-ONLY</p>','Prohibited content')
    def test_unreviewed_html(self): self.reject('extra.html',b'<p>Unreviewed</p>')
    def test_changed_file(self): self.reject('styles.css',b'body { color: red; }')
    def test_private_link(self): self.reject('extra.html',b'<a href="../coursework/private.py">Details</a>','Public boundary escape')
    def test_good_output(self): self.assertEqual(validate(self.target)['courses'],29)
    def test_domain_root_link(self): self.reject('extra.html',b'<a href="/index.html">Home</a>','Root URL bypasses')
    def test_unapproved_source(self): self.reject('extra.html',b'<a href="https://github.com/scoggeshall/coursework-portfolio/blob/main/private.txt">Code</a>','Unreviewed source link')
    def test_contact_link(self): self.reject('extra.html',b'<a href="mailto:example@example.invalid">Contact</a>','Personal contact link')
    def test_missing_fragment(self): self.reject('extra.html',b'<a href="index.html#nonexistent">Home</a>','Missing fragment')
    def test_missing_file(self): self.reject('extra.html',b'<img src="absent.png" alt="test">','Missing target')

if __name__=='__main__': unittest.main()
