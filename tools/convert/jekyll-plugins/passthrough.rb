# Conversion helper: render Liquid only and keep Markdown as Markdown.
module Jekyll
  class StPassthrough < Converter
    safe true
    priority :highest
    def matches(ext); ext =~ /^\.md$/i; end
    def output_ext(ext); ".md"; end
    def convert(content); content; end
  end
  module Filters
    def markdownify(input); input.to_s; end
  end
  Hooks.register :pages, :pre_render do |page|
    page.data['layout'] = nil
  end
end
module Jekyll
  module Tags
    class IncludeTag
      alias_method :st_orig_render, :render
      def render(context)
        st_orig_render(context)
      rescue IOError, ArgumentError => e
        f = (render_variable(context) || @file) rescue @file
        "\n<!-- ST-MISSING-INCLUDE: #{f} -->\n"
      end
    end
  end
end
