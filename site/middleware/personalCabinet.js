export default function ({ route, redirect, $auth }) {
  if (!$auth.loggedIn) {
    return redirect('/');
  }
}
