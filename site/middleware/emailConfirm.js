export default function ({ route, redirect, $cookies }) {
  const isRegistered = $cookies.get('registration');

  if (isRegistered) {
    redirect('/verificationEmail');
  }
}
