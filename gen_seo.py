import os
import re

root = "/tmp/remake-waitlist-seo"
index_path = os.path.join(root, "index.html")
sitemap_path = os.path.join(root, "sitemap.xml")
products_dir = os.path.join(root, "products")
seo_slug = "bismuth-oxychloride-acne-safe.html"

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

header_match = re.search(r'(.*?)(</header>)(.*?)(<!-- Luxurious Footer -->.*)', index_html, re.DOTALL)
if header_match:
    pre_main = header_match.group(1) + header_match.group(2)
    post_main_and_footer = header_match.group(4)
else:
    print("Failed to parse index.html")
    exit(1)
    
seo_title = "Is Bismuth Oxychloride Acne Safe? • REMAKE Chemical Audit"
seo_description = "We reviewed Bismuth Oxychloride. Find out if this common makeup ingredient causes cystic acne, clogged pores, and ruins your skin barrier."
seo_h1 = "Is Bismuth Oxychloride Acne Safe?"
seo_keyword = "Bismuth Oxychloride"

pre_main = re.sub(r'<title>.*?</title>', f'<title>{seo_title}</title>', pre_main)
pre_main = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{seo_description}">', pre_main)
pre_main = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{seo_title}">', pre_main)
pre_main = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{seo_description}">', pre_main)
pre_main = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://remake.beauty/products/{seo_slug}">', pre_main)

# Fix asset links for subfolder nesting
pre_main = pre_main.replace('href="./', 'href="/')
pre_main = pre_main.replace('src="./', 'src="/')
pre_main = pre_main.replace("bg-[url('./", "bg-[url('/")

new_main_content = f"""
    <!-- SEO Main Content -->
    <section class="pt-24 pb-16 px-6 relative overflow-hidden bg-[var(--rhode-white)]">
      <div class="max-w-4xl mx-auto text-center relative z-10 mt-12">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-red-50 border border-red-100 rounded-full mb-6">
          <span class="w-1.5 h-1.5 rounded-full bg-red-400"></span>
          <span class="text-[10px] font-medium tracking-widest text-red-800 uppercase font-sans">Chemical Audit</span>
        </div>
        <h1 class="font-serif text-4xl md:text-6xl mb-6 text-[#2A2421] leading-[1.1] tracking-tight">{seo_h1}</h1>
        <p class="text-[#7C726E] text-base md:text-lg font-light max-w-2xl mx-auto leading-relaxed font-sans">
          It gives your foundation that "flawless, glowing finish," but for acne-prone skin, it is a silent nightmare. Here is why {seo_keyword} might be destroying your skin barrier.
        </p>
      </div>
    </section>

    <section class="py-12 px-6">
      <div class="max-w-3xl mx-auto">
        <div class="card-luxury p-8 md:p-12 mb-12 border border-[#F5DDE3] bg-white shadow-sm" style="border-radius: 20px;">
          <h2 class="font-serif text-3xl mb-6 text-[#2A2421]">What is {seo_keyword}?</h2>
          <p class="text-[#7C726E] font-light mb-6 font-sans">
            Bismuth Oxychloride is a synthetic pigment with an incredibly heavy molecular structure. It is synthetically derived from bismuth (a heavy metal byproduct of lead and copper refining), combined with chloride and oxygen. Brands love it because it imparts an immediate, pearl-like radiance and helps powders adhere perfectly to the skin. 
          </p>
          <p class="text-[#7C726E] font-light mb-6 font-sans">
            You will find it hiding in countless mineral powders, "clean" foundations, and high-end blushes. But this synthetic shimmer comes at a devastating cost for sensitive and acne-prone biology.
          </p>

          <h2 class="font-serif text-3xl mb-6 mt-12 text-[#2A2421]">Why It Ruins Your Skin Barrier</h2>
          
          <div class="grid gap-4 mb-8 font-sans">
            <div class="flex items-start gap-4 p-5 rounded-2xl bg-[#FFF0F3] border border-[#F5DDE3]">
              <div class="w-8 h-8 shrink-0 rounded-full bg-[#E8A0AA] flex items-center justify-center text-white font-bold text-sm">1</div>
              <div>
                <h3 class="font-medium text-[#2A2421] mb-1">Microscopic Needle Structure</h3>
                <p class="text-sm text-[#7C726E] font-light">Under a microscope, Bismuth Oxychloride crystals have sharp, jagged edges. When you buff them into your skin with a makeup brush, they act like micro-needles, physically scratching and compromising your lipid barrier.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-5 rounded-2xl bg-[#FFF0F3] border border-[#F5DDE3]">
              <div class="w-8 h-8 shrink-0 rounded-full bg-[#E8A0AA] flex items-center justify-center text-white font-bold text-sm">2</div>
              <div>
                <h3 class="font-medium text-[#2A2421] mb-1">Cystic Acne Trigger</h3>
                <p class="text-sm text-[#7C726E] font-light">Because it is uniquely heavy and adheres so strongly to the skin, it sinks deep into pores. Sweat and sebum mix with the heavy crystals, creating an impenetrable plug that erupts into painful, deep cystic acne.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-5 rounded-2xl bg-[#FFF0F3] border border-[#F5DDE3]">
              <div class="w-8 h-8 shrink-0 rounded-full bg-[#E8A0AA] flex items-center justify-center text-white font-bold text-sm">3</div>
              <div>
                <h3 class="font-medium text-[#2A2421] mb-1">Severe Itching & Irritation</h3>
                <p class="text-sm text-[#7C726E] font-light">Many people report a strange "itching" sensation when they sweat while wearing mineral makeup. That is the Bismuth Oxychloride reacting with moisture and mechanically irritating the nerve endings in your compromised skin.</p>
              </div>
            </div>
          </div>

          <div class="bg-[var(--rhode-white)] p-8 mt-12 text-center border border-[#F5DDE3]" style="border-radius: 20px;">
            <h2 class="font-serif text-2xl mb-4 text-[#2A2421]">Stop Guessing. Start Scanning.</h2>
            <p class="text-[#7C726E] font-light mb-6 text-sm max-w-lg mx-auto font-sans">
              Sephora reviews won't tell you if a product contains Bismuth Oxychloride. REMAKE does. Scan any barcode to instantly expose toxic, pore-clogging ingredients hidden in the fine print.
            </p>
            <a href="/" class="btn-primary">
              Download REMAKE Free
            </a>
          </div>
        </div>
      </div>
    </section>
"""

# Fix links in post_main_and_footer
post_main_and_footer = post_main_and_footer.replace('href="./', 'href="/')
post_main_and_footer = post_main_and_footer.replace('src="./', 'src="/')

# Add the new link to the footer in post_main_and_footer
new_link = f'        <a href="/products/{seo_slug}" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">{seo_keyword} Chemical Audit</a>\n'
post_main_and_footer = post_main_and_footer.replace('      </div>\n    </div>\n</footer>', new_link + '      </div>\n    </div>\n</footer>')

with open(os.path.join(products_dir, seo_slug), "w", encoding="utf-8") as f:
    f.write(pre_main + "\n" + new_main_content + "\n" + post_main_and_footer)

# Update index.html footer
new_index = index_html.replace('      </div>\n    </div>\n</footer>', new_link + '      </div>\n    </div>\n</footer>')
with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_index)

# Update sitemap.xml
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_sitemap_url = f'''  <url>
    <loc>https://remake.beauty/products/{seo_slug}</loc>
    <priority>0.7</priority>
  </url>
</urlset>'''

sitemap = sitemap.replace('</urlset>', new_sitemap_url)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
    
print("Success")