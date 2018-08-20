from django.test import TestCase

from markup import wakaba


class NestedTagsTest(TestCase):
    def _get_url_by_hid(self, hid: str) -> str:
        return 'http://example.com/#{0}'.format(hid)

    def test_em_plus_strong(self):
        self.assertEqual(
            wakaba.make_all_inline_tags('*nomad*', self._get_url_by_hid),
            '<em>nomad</em>'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('* *nomad* *', self._get_url_by_hid),
            '* <em>nomad</em> *'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('**nomad**', self._get_url_by_hid),
            '<strong>nomad</strong>'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('***nomad***', self._get_url_by_hid),
            '***nomad***'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('** *nomad* **', self._get_url_by_hid),
            '** <em>nomad</em> **'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('* **nomad** *', self._get_url_by_hid),
            '* <strong>nomad</strong> *'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('** **nomad** **', self._get_url_by_hid),
            '** <strong>nomad</strong> **'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('** __nomad__ **', self._get_url_by_hid),
            '** <strong>nomad</strong> **'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('__ *nomad* __', self._get_url_by_hid),
            '__ <em>nomad</em> __'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('_ **nomad** _', self._get_url_by_hid),
            '_ <strong>nomad</strong> _'
        )

    def test_multi_words(self):
        self.assertEqual(
            wakaba.make_all_inline_tags('**nomad**huita**', self._get_url_by_hid),
            '<strong>nomad**huita</strong>'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('**nomad** atata **huita**', self._get_url_by_hid),
            '<strong>nomad</strong> atata <strong>huita</strong>'
        )

        self.assertEqual(
            wakaba.make_all_inline_tags('__nomad__ atata **huita**', self._get_url_by_hid),
            '<strong>nomad</strong> atata <strong>huita</strong>'
        )

    def test_other_combined_tags(self):
        self.assertEqual(
            wakaba.make_all_inline_tags('**&gt;&gt;0x100500**', self._get_url_by_hid),
            '<strong><a class="ref" href="http://example.com/#0x100500">&gt;&gt;0x100500</a></strong>'
        )

        self.assertNotEqual(
            wakaba.make_all_inline_tags('--http://example.com--', self._get_url_by_hid),
            '<s><a href="http://example.com" rel="nofollow">http://example.com</a></s>'
        )
