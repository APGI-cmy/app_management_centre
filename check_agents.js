const fs = require('fs');
const yaml = require('js-yaml');

const files = fs.readdirSync('.github/agents').filter(f => f.endsWith('.md') && !f.startsWith('_'));
for (const fname of files.sort()) {
  const content = fs.readFileSync('.github/agents/' + fname, 'utf8');
  if (!content.startsWith('---')) { console.log(fname + ': NO FRONTMATTER'); continue; }
  const end = content.indexOf('\n---\n', 3);
  if (end === -1) { console.log(fname + ': UNCLOSED FM'); continue; }
  const fm = content.slice(3, end);
  try {
    const data = yaml.load(fm);
    const metaCount = data.metadata ? Object.keys(data.metadata).length : 0;
    const descLen = data.description ? data.description.length : 0;
    const descBytes = data.description ? Buffer.byteLength(data.description, 'utf8') : 0;
    console.log(fname + ': OK (meta=' + metaCount + ', desc=' + descLen + 'ch/' + descBytes + 'B)');
  } catch(e) {
    console.log(fname + ': YAML ERROR: ' + e.message.substring(0, 120));
  }
}
