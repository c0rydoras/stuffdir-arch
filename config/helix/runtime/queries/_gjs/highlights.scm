(call_expression
  function: (identifier) @function)

(call_expression
  function: (member_expression
    property: (property_identifier) @function.method))

[
  (glimmer_opening_tag)
  (glimmer_closing_tag)
] @variable.builtin
