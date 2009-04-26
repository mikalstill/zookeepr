<%inherit file="/base.mako" />

    <h2>Voucher Codes</h2>

% if c.admin:
    <p>This table lists all the voucher codes.</p>
% else:
    <p>This table lists the voucher codes for your group.</p>
%   if not c.vouchers:
    <p>(Note: you do not appear to be a group leader, so the table is blank.)</p>
%   endif
% endif

    <table>
      <tr>
        <th>Code</th>
        <th>Products</th>
% if c.admin:
        <th>Leader</th>
% endif
        <th>Comment</th>
        <th>Used By</th>
%   if c.admin:
        <th>&nbsp;</th>
%   endif
      </tr>

% for voucher in c.vouchers:
      <tr class="${ h.cycle('even', 'odd')}">
        <td>${ voucher.code }</td>
        <td>
%   if voucher.products:
%       for vproduct in voucher.products:
         ${ vproduct.percentage }% discount off ${ vproduct.qty } x ${ vproduct.product.description }<br>
%       endfor
%   endif
        </td>
%   if c.admin:
        <td>
%       if voucher.leader:
          ${ voucher.leader.firstname |h} ${ voucher.leader.lastname |h}
          &lt;${ voucher.leader.email_address |h}&gt;
%       else:
          (no leader)
%       endif
        </td>
%   endif
        <td>${ voucher.comment |h}</td>
%   if voucher.registration:
        <td>${ voucher.registration.person.firstname } ${ voucher.registration.person.lastname }
%          if voucher.registration.person.company:
           ${ "(" + voucher.registration.person.company + ")"}
%          endif
           &lt;${ voucher.registration.person.email_address }&gt;
        </td>
%   else:
        <td><strong>Hasn't been used</strong></td>
%       if c.admin:
        <td>${ h.link_to('delete', url=h.url_for(action='delete', id=voucher.id)) }</td>
%       endif
%   endif

      </tr>
% endfor

    </table>

% if c.admin:
    <br>
    <p>${ h.link_to('Add another', url=h.url_for(controller='voucher', action='new')) }</p>
% endif
